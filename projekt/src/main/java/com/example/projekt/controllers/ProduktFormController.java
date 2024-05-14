package com.example.projekt.controllers;

import com.example.projekt.models.ProcentHelper;
import com.example.projekt.models.ProduktItem;
import com.example.projekt.models.User;
import com.example.projekt.repositories.ProduktItemRepository;
import com.example.projekt.services.ProduktItemService;
import com.example.projekt.services.UserService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import java.sql.Date;
import java.sql.Timestamp;
import java.util.*;
import java.util.stream.Collectors;

@Controller
public class ProduktFormController {
    @Autowired
    private ProduktItemService produktItemService;

    @Autowired
    private ProduktItemRepository produktItemRepository;

    @Autowired
    private UserService userService;

    @GetMapping("/create-produkt")
    public String showCreateForm(ProduktItem produktItem) {
        return "new-produkt-item";
    }

    @PostMapping("/produkt")
    public String createTodoItem(@Valid ProduktItem produktItem, BindingResult result, Model model) {
        if (produktItemService.getByEan(produktItem.getEan()).isEmpty()) {
            ProduktItem item = new ProduktItem();
            item.setNazwa(produktItem.getNazwa());
            item.setEan(produktItem.getEan());
            item.setTyp(produktItem.getTyp());
            item.setCena(produktItem.getCena());
            item.setProcent(produktItem.getProcent());
            item.setCzy_jest_przecena(produktItem.getCzy_jest_przecena());
            item.setIlosc(produktItem.getIlosc());

            Calendar cal = Calendar.getInstance();
            Timestamp ts2 = new Timestamp(System.currentTimeMillis());
            item.setData_ostatniej_zmiany(ts2);
            cal.setTime(ts2);
            cal.add(Calendar.DAY_OF_WEEK, 7);
            ts2.setTime(cal.getTime().getTime());
            item.setData_spozycia(Date.valueOf(String.valueOf(ts2.toLocalDateTime().toLocalDate())));


            produktItemService.saveNew(item);
            return "redirect:/index-pracownik?success";
        }
        return "redirect:/index-pracownik?fail";
    }

    @GetMapping("/edit/{id}")
    public String showUpdateForm(@PathVariable("id") Long ean, Model model) {
        ProduktItem produktItem = produktItemService
                .getByEan(ean)
                .orElseThrow(() -> new IllegalArgumentException("ProduktItem ean: " + ean + " not found"));

        model.addAttribute("produkt", produktItem);
        return "edit-produkt-item";
    }

    @PostMapping("/produkt/{ean}")
    public String updateProduktItem(@PathVariable("ean") Long ean, @Valid ProduktItem produktItem, BindingResult result, Model model) {

        ProduktItem item = produktItemService
                .getByEan(ean)
                .orElseThrow(() -> new IllegalArgumentException("ProduktItem ean: " + ean + " not found"));

        item.setCzy_jest_przecena(produktItem.getCzy_jest_przecena());
        item.setNazwa(produktItem.getNazwa());
        item.setCena(produktItem.getCena());
        item.setIlosc(produktItem.getIlosc());
        item.setProcent(produktItem.getProcent());
        item.setTyp(produktItem.getTyp());

        produktItemService.save(item);

        return "redirect:/index-pracownik";
    }

    @GetMapping("/delete/{id}")
    public String deleteProduktItem(@PathVariable("id") Long ean, Model model) {
        ProduktItem produktItem = produktItemService
                .getByEan(ean)
                .orElseThrow(() -> new IllegalArgumentException("ProduktItem ean: " + ean + " not found"));

        produktItemService.delete(produktItem);
        return "redirect:/index-pracownik";
    }

    @GetMapping("/newsletterAdd/{id}")
    public String dodajDoNewsletter(@PathVariable("id") Long ean, Model model) {
        ProduktItem produktItem = produktItemService
                .getByEan(ean)
                .orElseThrow(() -> new IllegalArgumentException("ProduktItem ean: " + ean + " not found"));

        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        String username = auth.getName();
        User user = userService.getUserByUsername(username);

        Set<ProduktItem> newsletter = user.getProduktItems();

        boolean czy_jest = false;
        if (!(newsletter.isEmpty())) {
            czy_jest = false;
            Optional<ProduktItem> produkt = produktItemRepository.findByEan(ean);
            Iterator<ProduktItem> newsletterIterator = newsletter.iterator();
            while (newsletterIterator.hasNext()){
                Long e = newsletterIterator.next().getEan();
                System.out.println(e+" ddddddddddd");
                System.out.println(ean + " ddddddddddd");
                if(e.equals(ean)){
                    System.out.println("rowna sie ddddddddddd");
                    czy_jest = true;
                }
            }
            if (!czy_jest) {
                newsletter.add(produkt.get());
            }
        } else {
            System.out.println("poczatek? ddddddddddd");
            newsletter = new HashSet<>();
            Optional<ProduktItem> produkt = produktItemRepository.findByEan(ean);
            newsletter.add(produkt.get());
        }
        user.setProduktItems(newsletter);
        userService.saveNewsletter(user);
        System.out.println("poszlo ddddddddddd");
        if(czy_jest){
            return "redirect:/index-klient?newsletterBylo";
        }
        return "redirect:/index-klient?newsletterDodano";
    }

    @GetMapping("/newsletter")
    public String showNewsletter( Model model) {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        String username = auth.getName();
        User user = userService.getUserByUsername(username);
        Set<ProduktItem> newsletter = user.getProduktItems();
        List<ProduktItem> sortedList = newsletter.stream()
                .sorted(Comparator.comparing(ProduktItem::getData_ostatniej_zmiany))
                .collect(Collectors.toList());
        Collections.reverse(sortedList);

        model.addAttribute("produktItems", sortedList);
        model.addAttribute( "procentHelper", ProcentHelper.getInstance() );
        return "newsletter";
    }

    @GetMapping("/newsletterDelete/{id}")
    public String usunZNewsletter(@PathVariable("id") Long ean, Model model) {
        ProduktItem produktItem = produktItemService
                .getByEan(ean)
                .orElseThrow(() -> new IllegalArgumentException("ProduktItem ean: " + ean + " not found"));

        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        String username = auth.getName();
        User user = userService.getUserByUsername(username);

        Set<ProduktItem> newsletter = user.getProduktItems();

        if (!(newsletter.isEmpty())) {
            boolean czy_jest = false;
            Optional<ProduktItem> produkt = produktItemRepository.findByEan(ean);
            Iterator<ProduktItem> newsletterIterator = newsletter.iterator();
            while (newsletterIterator.hasNext()){
                ProduktItem pi = newsletterIterator.next();
                Long e = pi.getEan();
                System.out.println(e+" ddddddddddd");
                System.out.println(ean + " ddddddddddd");
                if(e.equals(ean)){
                    System.out.println("rowna sie ddddddddddd");
                    newsletter.remove(pi);
                    break;
                }
            }
        }
        user.setProduktItems(newsletter);
        userService.saveNewsletter(user);
        System.out.println("poszlo ddddddddddd");
        return "redirect:/newsletter?delete";
    }
}
