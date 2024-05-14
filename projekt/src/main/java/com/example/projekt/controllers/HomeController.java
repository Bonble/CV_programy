package com.example.projekt.controllers;

import com.example.projekt.models.ProcentHelper;
import com.example.projekt.models.ProduktItem;
import com.example.projekt.services.ProduktItemService;
import jakarta.validation.Valid;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@Controller
public class HomeController {

    @Autowired
    private ProduktItemService produktItemService;



    @GetMapping("/")
    public ModelAndView index(ProduktItem produktItem) {
        ModelAndView modelAndView = new ModelAndView("index");
        Collection auth = SecurityContextHolder.getContext().getAuthentication().getAuthorities();
        String rola = auth.toString();
        if(rola.equals("[ROLE_KLIENT]")){
            modelAndView = new ModelAndView("index-klient");
        }
        if(rola.equals("[ROLE_PRACOWNIK]")){
            modelAndView = new ModelAndView("index-pracownik");
        }
        modelAndView.addObject("produktItems", produktItemService.getAll());
        modelAndView.getModelMap().addAttribute( "procentHelper", ProcentHelper.getInstance() );/*
        Collection auth = SecurityContextHolder.getContext().getAuthentication().getAuthorities();
        String rola = auth.toString();
        System.out.println(rola); //[ROLE_ANONYMOUS] [ROLE_PRACOWNIK] [ROLE_KLIENT]
        modelAndView.getModelMap().addAttribute( "rola", rola );*/
        return modelAndView;
    }

    @PostMapping("/sort/{typ}")
    public ModelAndView indexTyp(@PathVariable("typ") String typ,@Valid ProduktItem produktItem, Model model) {
        ModelAndView modelAndView = new ModelAndView("index");
        modelAndView.getModelMap().addAttribute( "procentHelper", ProcentHelper.getInstance() );

        Set<ProduktItem> res = new HashSet<ProduktItem>();
        Iterable<ProduktItem> produktItems =  produktItemService.getAll();

        if(produktItem.getTyp().equals("Przecenione")){
            Iterator<ProduktItem> i = produktItems.iterator();
            while (i.hasNext()) {
                ProduktItem pi = i.next();
                if (pi.getCzy_jest_przecena()) {
                    res.add(pi);
                }
            }
            modelAndView.addObject("produktItems", res);
        }else if(produktItem.getTyp().equals("Wszystkie")){
            modelAndView.addObject("produktItems", produktItems);
        }else {
            Iterator<ProduktItem> i = produktItems.iterator();
            while (i.hasNext()) {
                System.out.println(produktItem.getTyp());
                ProduktItem pi = i.next();
                if (pi.getTyp().equals(produktItem.getTyp())) {
                    res.add(pi);
                }
            }
            modelAndView.addObject("produktItems", res);
        }
        return modelAndView;
    }


    @GetMapping("/index-klient")
    public ModelAndView index_klient(ProduktItem produktItem) {
        ModelAndView modelAndView = new ModelAndView("index-klient");
        modelAndView.addObject("produktItems", produktItemService.getAll());
        modelAndView.getModelMap().addAttribute( "procentHelper", ProcentHelper.getInstance() );
        return modelAndView;
    }

    @PostMapping("/index-klient/sort/{typ}")
    public ModelAndView indexTypKlient(@PathVariable("typ") String typ,@Valid ProduktItem produktItem, Model model) {
        ModelAndView modelAndView = new ModelAndView("index-klient");
        modelAndView.getModelMap().addAttribute( "procentHelper", ProcentHelper.getInstance() );

        Set<ProduktItem> res = new HashSet<ProduktItem>();
        Iterable<ProduktItem> produktItems =  produktItemService.getAll();

        if(produktItem.getTyp().equals("Przecenione")){
            Iterator<ProduktItem> i = produktItems.iterator();
            while (i.hasNext()) {
                ProduktItem pi = i.next();
                if (pi.getCzy_jest_przecena()) {
                    res.add(pi);
                }
            }
            modelAndView.addObject("produktItems", res);
        }else if(produktItem.getTyp().equals("Wszystkie")){
            modelAndView.addObject("produktItems", produktItems);
        }else {
            Iterator<ProduktItem> i = produktItems.iterator();

            while (i.hasNext()) {
                System.out.println(produktItem.getTyp());
                ProduktItem pi = i.next();
                if (pi.getTyp().equals(produktItem.getTyp())) {
                    res.add(pi);
                }
            }
            modelAndView.addObject("produktItems", res);
        }
        return modelAndView;
    }

    @GetMapping("/index-pracownik")
    public ModelAndView index_pracownik(ProduktItem produktItem) {
        ModelAndView modelAndView = new ModelAndView("index-pracownik");
        modelAndView.addObject("produktItems", produktItemService.getAll());
        modelAndView.getModelMap().addAttribute( "procentHelper", ProcentHelper.getInstance() );
        return modelAndView;
    }

    @PostMapping("/index-pracownik/sort/{typ}")
    public ModelAndView indexTypPracownik(@PathVariable("typ") String typ,@Valid ProduktItem produktItem, Model model) {
        ModelAndView modelAndView = new ModelAndView("index-pracownik");
        modelAndView.getModelMap().addAttribute( "procentHelper", ProcentHelper.getInstance() );

        Set<ProduktItem> res = new HashSet<ProduktItem>();
        Iterable<ProduktItem> produktItems =  produktItemService.getAll();

        if(produktItem.getTyp().equals("Przecenione")){
            Iterator<ProduktItem> i = produktItems.iterator();
            while (i.hasNext()) {
                ProduktItem pi = i.next();
                if (pi.getCzy_jest_przecena()) {
                    res.add(pi);
                }
            }
            modelAndView.addObject("produktItems", res);
        }else if(produktItem.getTyp().equals("Wszystkie")){
            modelAndView.addObject("produktItems", produktItems);
        }else {
            Iterator<ProduktItem> i = produktItems.iterator();

            while (i.hasNext()) {
                System.out.println(produktItem.getTyp());
                ProduktItem pi = i.next();
                if (pi.getTyp().equals(produktItem.getTyp())) {
                    res.add(pi);
                }
            }
            modelAndView.addObject("produktItems", res);
        }
        return modelAndView;
    }

    @GetMapping("/login")
    public String logowanie(){
        return "login";
    }

    @GetMapping("/login_alt")
    public String login(){
        return "login_alt";
    }

    @GetMapping("/logout")
    public String logout() {
        return "redirect:/login";
    }


    @GetMapping("/profil")
    public String showUserProfile (Model model){
        //Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        //String currentPrincipalName = authentication.getName();
        //User user = userRepository.findByEmail(authentication.getPrincipal());
        //model.addAttribute("currentUser", user);
        return "profil";
    }


}
