package com.example.projekt.models;

import java.math.BigDecimal;

import static java.math.BigDecimal.ROUND_HALF_DOWN;

public class ProcentHelper {
    private static ProcentHelper procentHelper;
    private ProcentHelper(){ }

    public static ProcentHelper getInstance() {
        if (procentHelper == null)
            procentHelper=new ProcentHelper();
        return procentHelper;
    }

    public BigDecimal obliczProcent(BigDecimal cena, boolean przecena, Long procent){
        if(przecena){
            float p=(float) procent/100;
            return cena.multiply(BigDecimal.valueOf(1.0-p)).setScale(2,ROUND_HALF_DOWN);
        }else{
            return cena;
        }
    }
}
