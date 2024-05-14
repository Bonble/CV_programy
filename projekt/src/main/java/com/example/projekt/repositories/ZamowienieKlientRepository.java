package com.example.projekt.repositories;

import com.example.projekt.models.ProduktItem;
import com.example.projekt.models.ZamowienieKlient;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ZamowienieKlientRepository  extends JpaRepository<ZamowienieKlient, Long> {
    Optional<ZamowienieKlient> findById(Integer id);
}
