import java.util.LinkedList;
import java.util.List;

public class Wierzcholek {
    String nazwa;
    List <Krawedz> krawedzie = new LinkedList<>();
    int koszt;
    Wierzcholek poprzednik;
    boolean obslozony;

    Wierzcholek(String nazwa){
        this.nazwa=nazwa;
        koszt = Integer.MAX_VALUE;
        poprzednik = this;
        obslozony = false;
    }

    @Override
    public boolean equals(Object obj) {
        if(!(obj instanceof Wierzcholek)){
            return false;
        }
        else {
            Wierzcholek v = (Wierzcholek) obj;
            return v.nazwa.equals(this.nazwa);
        }
    }

    @Override
    public String toString() {
        String linia = nazwa + " -> ";
        if (nazwa != poprzednik.nazwa) {
            linia = nazwa + "[" + koszt + " , " + poprzednik.nazwa + " ] " + " -> ";
        }
        for (Krawedz k : krawedzie) {
            linia += k;
        }
        return linia;
    }

    void zrelaksujKrawedzie(){
        for(Krawedz k : krawedzie){
            if(k.dokad.koszt > k.skad.koszt + k.waga) {
                k.dokad.koszt = k.skad.koszt + k.waga;
                k.dokad.poprzednik = k.skad;
            }
        }
    }

    int liczba_krawedzi(){
        return krawedzie.size();
    }

}