package com.example.projekt.controllers;

import com.example.projekt.models.ProduktItem;
import com.example.projekt.models.User;
import com.example.projekt.models.ZamowienieKlient;
import com.example.projekt.services.ProduktItemService;
import com.example.projekt.services.UserService;
import com.example.projekt.services.ZamowienieKlientService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

import java.math.BigDecimal;
import java.sql.Date;
import java.sql.Timestamp;
import java.util.*;

import static java.math.BigDecimal.ROUND_HALF_DOWN;

@Controller
public class ZamowieniaController {
    @Autowired
    private ProduktItemService produktItemService;

    @Autowired
    private UserService userService;

    @Autowired
    private ZamowienieKlientService zamowienieKlientService;

    @PostMapping("/zamow_klient")
    public String dodajZamowienieKlient(@Valid ProduktItem produktItem, Model model) {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        Collection<? extends GrantedAuthority> zalogowany = authentication.getAuthorities();
        System.out.println(zalogowany);
        //System.out.println(Objects.isNull(produktItem.getIlosc()));
        if(!Objects.isNull(produktItem.getIlosc())){
            if (produktItemService.getByEan(produktItem.getEan()).isPresent()) {
                ProduktItem pi = produktItemService.getByEan(produktItem.getEan()).get();

                /*Iterator<ZamowienieKlient> zamowienia = zamowienieKlientService.getAll().iterator();
                Long ilosc = produktItem.getIlosc();
                while (zamowienia.hasNext()) {
                    ZamowienieKlient z = zamowienia.next();
                    if (Objects.equals(z.getProdukt_ean().getEan(), produktItem.getEan())) {
                        ilosc += z.getIlosc();
                    }

                    if(zalogowany.toString().equals("[ROLE_KLIENT]")) {
                        if (ilosc > pi.getIlosc()) {
                            return "redirect:/index-klient?zamowNieDodano";
                        }
                    }
                    //if (ilosc > pi.getIlosc()) {
                        //return "redirect:/index-klient?zamowNieDodano";
                    //}
                }*/
                System.out.println(produktItem.getIlosc().toString());
                System.out.println(pi.getIlosc().toString());
                if (pi.getIlosc() + 1 > produktItem.getIlosc() || zalogowany.toString().equals("[ROLE_PRACOWNIK]")) {
                    ZamowienieKlient zamowienie = new ZamowienieKlient();

                    String zalogowanyLogin = authentication.getName();
                    User user = userService.getUserByUsername(zalogowanyLogin);
                    zamowienie.setUser_id(user);

                    zamowienie.setProdukt_ean(pi);

                    zamowienie.setIlosc(produktItem.getIlosc());

                    zamowienie.setCzy_dostarczono(false);
                    Collection<? extends GrantedAuthority> role = authentication.getAuthorities();
                    if(role.toString().equals("[ROLE_PRACOWNIK]")){
                        zamowienie.setKoszt(pi.getCena().multiply(BigDecimal.valueOf(produktItem.getIlosc())).multiply(BigDecimal.valueOf(0.9f)));
                    }else {
                        if (pi.getCzy_jest_przecena()) {
                            BigDecimal procent = BigDecimal.valueOf(pi.getProcent() / 100.0);
                            BigDecimal cena = pi.getCena().multiply(procent).setScale(2, ROUND_HALF_DOWN);
                            zamowienie.setKoszt(cena.multiply(BigDecimal.valueOf(produktItem.getIlosc())));
                        } else {
                            zamowienie.setKoszt(pi.getCena().multiply(BigDecimal.valueOf(produktItem.getIlosc())));
                        }
                        pi.setIlosc(pi.getIlosc() - produktItem.getIlosc());
                        produktItemService.saveNew(pi);
                    }

                    Calendar cal = Calendar.getInstance();
                    Timestamp ts2 = new Timestamp(System.currentTimeMillis());
                    cal.setTime(ts2);
                    cal.add(Calendar.DAY_OF_WEEK, 4);
                    ts2.setTime(cal.getTime().getTime());
                    zamowienie.setData_dostarczenia(Date.valueOf(String.valueOf(ts2.toLocalDateTime().toLocalDate())));

                    zamowienieKlientService.save(zamowienie);
                    if(zalogowany.toString().equals("[ROLE_KLIENT]")) {
                        return "redirect:/index-klient?zamowDodano";
                    }
                    if(zalogowany.toString().equals("[ROLE_PRACOWNIK]")) {
                        return "redirect:/index-pracownik?zamowDodano";
                    }
                }
            }
        }
        if(zalogowany.toString().equals("[ROLE_PRACOWNIK]")) {
            return "redirect:/index-pracownik?zamowNieDodano";
        }
        return "redirect:/index-klient?zamowNieDodano";
    }

    @GetMapping("/zamowieniaKlient")
    public String zamowieniaKlientShow(Model model){
        Iterator<ZamowienieKlient> zamowienia = zamowienieKlientService.getAll().iterator();

        Set<ZamowienieKlient> zamowieniaKlienta = new HashSet<>();

        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        String zalogowany = authentication.getName();
        User user = userService.getUserByUsername(zalogowany);
        while (zamowienia.hasNext()){
            ZamowienieKlient z = zamowienia.next();
            if(user.getId().equals(z.getUser_id().getId())){
                zamowieniaKlienta.add(z);
            }
        }
        model.addAttribute("zamowienia", zamowieniaKlienta);
        return "zamowieniaKlient";
    }
    @GetMapping("/potwierdzZamowKlient/{id}")
    public String zamowieniaKlientPotwierdz(@PathVariable("id") Integer id, Model model) {
        ZamowienieKlient zamowienieKlient = zamowienieKlientService.getById(id).get();
        zamowienieKlient.setCzy_dostarczono(true);
        ProduktItem produktItem = produktItemService.getByEan(zamowienieKlient.getProdukt_ean().getEan()).get();

        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        Collection<? extends GrantedAuthority> zalogowanyRola = authentication.getAuthorities();
        System.out.println(zalogowanyRola);
        if(zalogowanyRola.toString().equals("[ROLE_KLIENT]")) {
            System.out.println("klient");
        }
        if(zalogowanyRola.toString().equals("[ROLE_PRACOWNIK]")){
            produktItem.setIlosc(produktItem.getIlosc() + zamowienieKlient.getIlosc());
            produktItemService.save(produktItem);
        }
        zamowienieKlientService.save(zamowienieKlient);
        return "redirect:/zamowieniaKlient?potwierdzono";
    }

    @GetMapping("/usunZamowKlient/{id}")
    public String zamowieniaKlientUsun(@PathVariable("id") Integer id, Model model) {
        ZamowienieKlient zamowienieKlient = zamowienieKlientService.getById(id).get();
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        Collection<? extends GrantedAuthority> zalogowanyRola = authentication.getAuthorities();

        ProduktItem produktItem = produktItemService.getByEan(zamowienieKlient.getProdukt_ean().getEan()).get();

        if(zalogowanyRola.toString().equals("[ROLE_KLIENT]") && !zamowienieKlient.isCzy_dostarczono()) {
            produktItem.setIlosc(produktItem.getIlosc() + zamowienieKlient.getIlosc());
            produktItemService.saveNew(produktItem);
        }
        zamowienieKlientService.delete(zamowienieKlient);
        return "redirect:/zamowieniaKlient?usunieto";
    }
}
