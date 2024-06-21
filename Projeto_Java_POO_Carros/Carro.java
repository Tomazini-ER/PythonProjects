package estudo_01;

public class Carro extends Automovel{
	public String buzinar() {
		return " buzina";
	}
	public Carro(String marca, String modelo, int ano, int quilometragem) {
        super(marca, modelo, ano, quilometragem);
    }

    public String imprimir() {
        return "Marca: " + getMarca() + ", Modelo: " + getModelo() + ", ano: " + getAno() 
        + "com " + getQuilometragem() + "Km rodados";
    }
}
