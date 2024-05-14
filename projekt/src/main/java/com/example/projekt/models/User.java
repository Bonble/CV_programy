package com.example.projekt.models;

import jakarta.persistence.*;
import jdk.jfr.Recording;
import lombok.Getter;
import lombok.Setter;
import org.hibernate.annotations.LazyCollection;
import org.hibernate.annotations.LazyCollectionOption;

import java.util.Collection;
import java.util.HashSet;
import java.util.Optional;
import java.util.Set;

@Getter
@Setter
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;


    private String adres;

    private String nazwisko;

    @Column(nullable=false, unique=true)
    private String email;

    @Column(nullable=false)
    private String password;
    @ManyToMany(cascade=CascadeType.ALL)
    @LazyCollection(LazyCollectionOption.FALSE)
    private Collection<Role> roles;



    @ManyToMany(cascade = { CascadeType.MERGE }, fetch = FetchType.EAGER)
    @JoinTable(
            name = "newsletter",
            joinColumns = { @JoinColumn(name = "id") },
            inverseJoinColumns = { @JoinColumn(name = "ean")})
    private Set<ProduktItem> produktItems = new HashSet<ProduktItem>();

    @OneToMany(mappedBy = "user_id", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private Set<ZamowienieKlient> zamowienia = new HashSet<>();

            /*@OneToOne(fetch = FetchType.LAZY)
            @JoinTable( name = "newsletter", joinColumns = @JoinColumn ( name = "question_id"), inverseJoinColumns = @JoinColumn( name = "option_id"))
            private Collection<ProduktItem> produktItems;*/

    public Collection<Role> getRoles() {
        return roles;
    }
    public void setRoles(Collection<Role> roles) {
        this.roles = roles;
    }

    /*
    public Set<ProduktItem> getNewsletter() {
        return produktItems;
    }

    public void setNewsletter(Set<ProduktItem> newsletters) {
        this.produktItems = newsletters;
    }*/



}