package com.example.projekt.models;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class LoginDto {
    private String username;
    private String password;
    public LoginDto() {
    }

}