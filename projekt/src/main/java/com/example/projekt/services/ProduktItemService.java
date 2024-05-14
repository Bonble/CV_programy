package com.example.projekt.services;

import com.example.projekt.models.ProduktItem;
import com.example.projekt.repositories.ProduktItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.sql.Date;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Optional;

@Service
public class ProduktItemService {

    private static final SimpleDateFormat sdf1 = new SimpleDateFormat("yyyy-MM-dd");
    private static final SimpleDateFormat sdf3 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    @Autowired
    private ProduktItemRepository produktItemRepository;

    public Optional<ProduktItem> getByEan(Long ean) {
        return produktItemRepository.findByEan(ean);
    }

    public Iterable<ProduktItem> getAll() {
        return produktItemRepository.findAll();
    }

    public ProduktItem save(ProduktItem produktItem) {
        Timestamp timestamp = new Timestamp(System.currentTimeMillis());

        produktItem.setData_ostatniej_zmiany(timestamp);
        return produktItemRepository.save(produktItem);
    }

    public ProduktItem saveNew(ProduktItem produktItem) {
        return produktItemRepository.save(produktItem);
    }

    public BigDecimal oblicz_przecene(Long id){
        Optional<ProduktItem> p = produktItemRepository.findById(id);
        if(p.get().getCzy_jest_przecena()) {
            return p.get().getCena().multiply(BigDecimal.valueOf(p.get().getProcent()/100));
        } else{
            return p.get().getCena();
        }
    }

    public void delete(ProduktItem produktItem) {
        produktItemRepository.delete(produktItem);
    }

}
