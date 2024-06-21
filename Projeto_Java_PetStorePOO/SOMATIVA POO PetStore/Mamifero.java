package PetStore;

import java.io.Serializable;
// serializable são os dados a serem persistidos
public abstract class Mamifero implements Serializable {

	private static final long serialVersionUID = 1L;
	private   String nome;
	private   int idade;
	private   String dono;
	protected String especie;
	
	public Mamifero(String nome, int idade, String dono) {
		this.nome = nome;
		this.idade = idade;
		this.dono = dono;
	}
	//aqui é tema da ATP utilizar classe mãe por meio da chamada SUPER
	//usar construtores: encadeamento de construtuores
	//usar sobrescrita @override
	//Com a sobrescrita, conseguimos especializar os métodos herdados das superclasses, alterando o seu comportamento nas subclasses por um mais específico.
	//
	//A sobrescrita de métodos consiste basicamente em criar um novo método na classe filha contendo a mesma assinatura e mesmo tipo de retorno do método sobrescrito.
	public String toString() {
		String retorno = "";
		retorno += "Nome: "     + this.nome     + "\n";
		retorno += "Idade: "    + this.idade    + " anos\n";
		retorno += "Dono: "     + this.dono     + "\n";
		retorno += "Especie: "  + this.especie  + "\n";
		retorno += "Barulho: "  + soar()        + "\n";
		return retorno;
	}
	public abstract String soar();
}
