package com.example.projekt.repositories;

import com.example.projekt.models.ProduktItem;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ProduktItemRepository extends JpaRepository<ProduktItem, Long>{
    Optional<ProduktItem> findByEan(Long ean);

    //Optional<ProduktItem> findByName(Long ean);
}
