package estudo_01;

public class Moto extends Automovel {	
	public String buzinar() {
		return " buzina";
	}
	public Moto(String marca, String modelo, int ano, int quilometragem) {    
    	super(marca, modelo, ano, quilometragem);
    }
    public String imprimir() {
        return "Marca: " + getMarca() + ", Modelo: " + getModelo() + 
            "Ano: " + getAno() + "com " + getQuilometragem() + "Km rodados"; 				
    }
}

