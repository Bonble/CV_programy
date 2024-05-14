package com.example.projekt.services;

import com.example.projekt.models.ProduktItem;
import com.example.projekt.models.User;
import com.example.projekt.models.UserRegisterDto;
import com.example.projekt.models.ZamowienieKlient;
import com.example.projekt.repositories.ZamowienieKlientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

@Service
public class ZamowienieKlientService {

    @Autowired
    ZamowienieKlientRepository zamowienieKlientRepository;

    public Iterable<ZamowienieKlient> getAll() {
        return zamowienieKlientRepository.findAll();
    }

    public Optional<ZamowienieKlient> getById(Integer id) {
        return zamowienieKlientRepository.findById(id);
    }

    public void delete(ZamowienieKlient zamowienieKlient) {
        zamowienieKlientRepository.delete(zamowienieKlient);
    }


    public ZamowienieKlient save(ZamowienieKlient zamowienie) {
    List<ZamowienieKlient> zamowienia = zamowienieKlientRepository.findAll();
    Iterator<ZamowienieKlient> i = zamowienia.iterator();
    while (i.hasNext()){
        ZamowienieKlient z = i.next();
        if(z.isCzy_dostarczono()==zamowienie.isCzy_dostarczono()) {
            if (z.getData_dostarczenia().equals(zamowienie.getData_dostarczenia()) && Objects.equals(z.getProdukt_ean().getEan(), zamowienie.getProdukt_ean().getEan()) && Objects.equals(z.getUser_id().getId(), zamowienie.getUser_id().getId())) {
                z.setKoszt(z.getKoszt().add(zamowienie.getKoszt()));
                z.setIlosc(z.getIlosc() + zamowienie.getIlosc());
                zamowienieKlientRepository.save(z);
                delete(zamowienie);
                return z;
            }
        }
    }
    zamowienieKlientRepository.save(zamowienie);
    return zamowienie;
    }
}
