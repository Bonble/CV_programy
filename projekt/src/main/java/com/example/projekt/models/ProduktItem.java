package com.example.projekt.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.springframework.format.annotation.DateTimeFormat;

import java.io.Serializable;
import java.math.BigDecimal;
import java.sql.Date;
import java.sql.Timestamp;
import java.util.HashSet;
import java.util.Set;

@Getter
@Setter
@Entity
@Table(name = "produkty")
public class ProduktItem implements Serializable {

    @Id
    private Long ean;


    private Long ilosc;

    private String nazwa;

    private String typ;

    private BigDecimal cena;

    private Boolean czy_jest_przecena;


    private Long procent;

    @DateTimeFormat(pattern = "dd-MM-yyyy")
    private Date data_spozycia;

    private Timestamp data_ostatniej_zmiany;


    @ManyToMany(mappedBy = "produktItems")
    private Set<User> newsletters = new HashSet<>();

    @OneToMany(mappedBy = "produkt_ean", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private Set<ZamowienieKlient> zamowienia = new HashSet<>();


    public Set<User> getNewslettery() {
        return newsletters;
    }

    public void setNewslettery(Set<User> newslettery) {
        this.newsletters = newslettery;
    }

    @Override
    public String toString() {
        return String.format("Produkt{ean=%d, nazwa='%s', czy_jest_przecena='%s', data_spozycia='%s', data_ostatniej_zmiany='%s'}",
                ean, nazwa, czy_jest_przecena, data_spozycia, data_ostatniej_zmiany);
    }

}
