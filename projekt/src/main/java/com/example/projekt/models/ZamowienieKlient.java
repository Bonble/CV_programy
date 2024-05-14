package com.example.projekt.models;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.Value;
import org.springframework.format.annotation.DateTimeFormat;

import java.math.BigDecimal;
import java.sql.Date;

@Getter
@Setter
@Entity
@Table(name = "zamowienia")
public class ZamowienieKlient {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user_id;
    //private Integer id_klienta;

    @ManyToOne
    @JoinColumn(name = "produkt_ean")
    private ProduktItem produkt_ean;
    //private Long ean;

    private Long ilosc;

    private BigDecimal koszt;

    @DateTimeFormat(pattern = "dd-MM-yyyy")
    private Date data_dostarczenia;

    private boolean czy_dostarczono;
}
