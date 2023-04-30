public class Krawedz {
    Wierzcholek skad;
    Wierzcholek dokad;
    int waga;

    Krawedz(Wierzcholek skad, Wierzcholek dokad, int waga){
        this.skad = skad;
        this.dokad = dokad;
        this.waga = waga;
    }

    @Override
    public String toString() {
        return dokad.nazwa + "[" + waga + "], ";
    }
}