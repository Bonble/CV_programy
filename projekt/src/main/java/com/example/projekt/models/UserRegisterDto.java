package com.example.projekt.models;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserRegisterDto {

    private String email;
    private String password;
    private String adres;
    private String nazwisko;
    public UserRegisterDto(){
    }


}