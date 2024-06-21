package estudo_01;

import java.io.Serializable;
public abstract class Automovel implements Serializable {
	private String marca;
	private String modelo;
	private int ano;
	private int quilometragem;

	public Automovel(String marca, String modelo, int ano, int quilometragem) {
		this.marca = marca;
		this.modelo = modelo;
		this.ano = ano;
		this.quilometragem = quilometragem;
	
	}
	public String getMarca() {
		return marca;
	}
	public String getModelo() {
		return modelo;
	}
	public int getAno() {
		return ano;
	}
	public int getQuilometragem() {
		return quilometragem;
	}
	public String toString() {
		String retorno = "";
		retorno += "Marca: "     + this.marca     + "\n";
		retorno += "Modelo: "    + this.modelo    + "\n";
		retorno += "Ano: "     + this.ano     + "\n";
		retorno += "Quilometragem: "  + this.quilometragem  + "Km\n";
		retorno += "Barulho: "  + buzinar()        + "\n";
		return retorno;
	}
	public abstract String buzinar();
}
