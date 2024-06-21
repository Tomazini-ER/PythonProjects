package estudo_01;

public class Onibus extends Automovel {
	private int assentos;
	public String buzinar() {
		return " buzina";
	}
	public Onibus(String marca, String modelo, int ano, int quilometragem, int assentos) {
		super(marca, modelo, ano, quilometragem);
		this.assentos = assentos;
	}
	public int getAssentos() {
		return assentos;
	}
	public String imprimir() {
		
	return "Marca: " + getMarca() + ", Modelo: " + getModelo() + ", ano: " + getAno() 
    + "com " + getAssentos() + " assentos";
}
}