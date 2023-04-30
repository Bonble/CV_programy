import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Graf {
    String nazwa;
    List <Wierzcholek> wierzcholki = new LinkedList<>();
    Graf (String nazwa){
        this.nazwa = nazwa;
    }

    @Override
    public String toString() {
        String linia =nazwa + "\n";
        for(Wierzcholek w : wierzcholki){
            linia += w + "\n";
        }
        return linia;
    }

    void dodajKrawedz(String skad, String dokad, int waga){
        Wierzcholek s = znajdz(skad);
        if(s == null){
            s = new Wierzcholek(skad);
            wierzcholki.add(s);
        }
        Wierzcholek d = znajdz(dokad);
        if(d == null){
            d = new Wierzcholek(dokad);
            wierzcholki.add(d);
        }
        Krawedz k = new Krawedz(s, d, waga);
        s.krawedzie.add(k);
    }

    Wierzcholek znajdz (String nazwa){
        int indeks = wierzcholki.indexOf(new Wierzcholek(nazwa));
        if(indeks == -1){
            return null;
        }
        return wierzcholki.get(indeks);
    }

    List<Wierzcholek>najmniejKrawedzi(){
        List<Wierzcholek>wynik = new LinkedList<>();
        int min = Integer.MAX_VALUE;
        for(Wierzcholek wierzcholek : wierzcholki){
            if(wierzcholek.krawedzie.size() < min){
                min=wierzcholek.krawedzie.size();
            }
        }
        for(Wierzcholek wierzcholek : wierzcholki){
            if(wierzcholek.krawedzie.size() == min){
                wynik.add(wierzcholek);
            }
        }

        return wynik;
    }

    List<Wierzcholek>najwiecejKrawedzi(){
        List<Wierzcholek>wynik = new LinkedList<>();
        int max = Integer.MIN_VALUE;
        for(Wierzcholek wierzcholek : wierzcholki){
            if(wierzcholek.krawedzie.size() > max){
                max=wierzcholek.krawedzie.size();
            }
        }
        for(Wierzcholek wierzcholek : wierzcholki){
            if(wierzcholek.krawedzie.size() == max){
                wynik.add(wierzcholek);
            }
        }

        return wynik;
    }

    Wierzcholek min(){
        Wierzcholek wynik=null;
        int m = Integer.MAX_VALUE;
        for(Wierzcholek w : wierzcholki){
            if(!w.obslozony && w.koszt < m) {
                wynik = w;
                m = w.koszt;
            }
        }
        return wynik;
    }

    void dijkstra(String nazwa){
        znajdz(nazwa).koszt = 0;
        Wierzcholek min = min();
        while(min!= null){
            min.zrelaksujKrawedzie();
            min.obslozony = true;
            min = min();
        }
    }

    String znajdzPolaczenie(String skad, String dokad){ // zwraca listę która jest połączeniem między dwoma wierzchołkami
        String wynik = "";
        dijkstra(skad);
        Wierzcholek s = znajdz(skad);
        Wierzcholek d = znajdz(dokad);
        Wierzcholek temp = d;
        while(!temp.equals(s)){
            wynik += (temp.nazwa + " ");
            temp=temp.poprzednik;
        }
        wynik += (s.nazwa + " ");
        return wynik;
    }


    void dodajZPliku(String nazwa) {
        File miasta = new File(nazwa);
        try {
            Scanner czytnik = new Scanner(miasta);
            while (czytnik.hasNextLine()) {
                String linia = czytnik.nextLine();
                char pierwszyZnak = linia.charAt(0);
                if (Character.compare('#', pierwszyZnak) != 0) {
                    String[] dane = linia.split(" ");
                    this.dodajKrawedz(dane[0], dane[1], Integer.parseInt(dane[2]));
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    Wierzcholek najwiekszy_wierzcholek(){ // zwraca krawędź której suma kosztów krawędzi zwróconych do niej jest największa
        int max=-1;
        Wierzcholek naj = min();
        for(Wierzcholek w: wierzcholki){
            int koszt=0;
            for(Wierzcholek w2: wierzcholki){
                for (Krawedz k: w2.krawedzie){
                    if(w.equals(k.dokad)){
                        koszt+=k.waga;
                    }
                }
            }
            if(koszt>max){
                max=koszt;
                naj = w;
            }
        }
        return naj;
    }

}