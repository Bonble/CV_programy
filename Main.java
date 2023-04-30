/*
Ten program w Javie tworzy graf z pliku dane.txt i wykonuje na nim operacje takie jak
sortowanie czy znalezienie drogi z jednego wierzchołka do drugiego
*/
import java.util.Collections;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        Graf g = new Graf("PB_");

        g.dodajZPliku("dane.txt");

        System.out.println(g);

        Collections.sort(g.wierzcholki, new Comparator<Wierzcholek>() { // sortuje graf na podstawie liczby krawędzi
            @Override
            public int compare(Wierzcholek o1, Wierzcholek o2) {
                return Comparator.comparing(Wierzcholek::liczba_krawedzi)
                        .compare(o1, o2);
            }
        });
        System.out.println(g);

        System.out.println("Najwiekszy wierzcholek: " + g.najwiekszy_wierzcholek());

        System.out.println(g.znajdzPolaczenie("B", "C"));

    }
}