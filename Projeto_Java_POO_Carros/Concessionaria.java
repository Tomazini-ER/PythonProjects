package estudo_01;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import javax.swing.JOptionPane;

public class Concessionaria {
	private ArrayList<Automovel> automoveis;
	public Concessionaria() {
		this.automoveis = new ArrayList<Automovel>();
	}
	public String[] leValores(String [] dadosIn) {
		String [] dadosOut = new String [dadosIn.length];
		for (int i =0; i < dadosIn.length; i++)
			dadosOut[i] = JOptionPane.showInputDialog("Por favor, entre com " + dadosIn[i] + ":");
		return dadosOut;
	}
	public Carro leCarro() {
		String [] valores = new String[4];
		String [] nomeVal = {"Marca", "Modelo", "Ano", "Quilometragem"};
		valores = leValores(nomeVal);
		int ano = this.retornaInteiro(valores[2]);
		int quilometragem = this.retornaInteiro(valores[3]);
		Carro carro = new Carro(valores[0], valores[1], ano, quilometragem);
		return carro;
		}
	public Onibus leOnibus() {
		String [] valores = new String[5];
		String [] nomeVal = {"Marca", "Modelo", "Ano","Quilometragem", "Assentos"};
		valores = leValores(nomeVal);
		int ano = this.retornaInteiro(valores[2]);
		int quilometragem = this.retornaInteiro(valores[3]);
		int assentos = this.retornaInteiro(valores[4]);
		Onibus onibus = new Onibus(valores[0], valores[1], ano, quilometragem, assentos);
		return onibus;
		}
	public Moto leMoto (){
		String [] valores = new String [4];
		String [] nomeVal = {"Marca", "Modelo", "Ano", "Quilometragem"};
		valores = leValores (nomeVal);
		int ano = this.retornaInteiro(valores[2]);
		int quilometragem = this.retornaInteiro(valores[3]);		
		Moto moto = new Moto (valores[0],valores[1], ano, quilometragem);
		return moto;
	}
		private boolean intValido(String s) {
			try {
				Integer.parseInt(s); 
				return true;
			} catch (NumberFormatException e) { 
				return false;
			}
		}
		public int retornaInteiro(String entrada) { 
			int numInt;
			while (!this.intValido(entrada)) {
				entrada = JOptionPane.showInputDialog(null, "Valor incorreto!\n\nDigite um número inteiro.");
			}
			return Integer.parseInt(entrada);
		}
		public void salvaAutomoveis (ArrayList<Automovel> automoveis){
			ObjectOutputStream outputStream = null;
			try {
				outputStream = new ObjectOutputStream 
						(new FileOutputStream("c:\\temp\\Concessionaria.dados"));
				for (int i=0; i < automoveis.size(); i++)
					outputStream.writeObject(automoveis.get(i));
			} catch (FileNotFoundException ex) {
				JOptionPane.showMessageDialog(null,"Impossível criar arquivo!");
				ex.printStackTrace();
			} catch (IOException ex) {
				ex.printStackTrace();
			} finally { 
				try {
					if (outputStream != null) {
						outputStream.flush();
						outputStream.close();
					}
				} catch (IOException ex) {
					ex.printStackTrace();
				}
			}
		}
		@SuppressWarnings("finally")
		public ArrayList<Automovel> recuperaAutomoveis (){
			ArrayList<Automovel> automoveisTemp = new ArrayList<Automovel>();

			ObjectInputStream inputStream = null;

			try {	
				inputStream = new ObjectInputStream
						(new FileInputStream("c:\\temp\\Concessionaria.dados"));
				Object obj = null;
				while ((obj = inputStream.readObject()) != null) {
					if (obj instanceof Automovel) {
						automoveisTemp.add((Automovel) obj);
					}   
				}          
			} catch (EOFException ex) { 
				System.out.println("Fim de arquivo.");
			} catch (ClassNotFoundException ex) {
				ex.printStackTrace();
			} catch (FileNotFoundException ex) {
				JOptionPane.showMessageDialog(null,"Arquivo com Automoveis NÃO existe!");
				ex.printStackTrace();
			} catch (IOException ex) {
				ex.printStackTrace();
			} finally {  
				try {
					if (inputStream != null) {
						inputStream.close();
					}
				} catch (final IOException ex) {
					ex.printStackTrace();
				}
				return automoveisTemp;
			}
		}
		public void menuConcessionaria (){

			String menu = "";
			String entrada;
			int    opc1, opc2;
			do {
				menu = "Controle Concessionaria\n" +
						"Opções:\n" + 
						"1. Entrar Automoveis\n" +
						"2. Exibir Automoveis\n" +
						"3. Limpar Automoveis\n" +
						"4. Gravar Automoveis\n" +
						"5. Recuperar Automoveis\n" +
						"6"
						+ ""
						+ ""
						+ ". Sair";
				entrada = JOptionPane.showInputDialog (menu + "\n\n");
				opc1 = this.retornaInteiro(entrada);
				switch (opc1) {
				case 1:
					menu = "Entrada de Automoveis\n" +
							"Opções:\n" + 
							"1. Carro\n" +
							"2. Moto\n" +
							"3. Ônibus";
					entrada = JOptionPane.showInputDialog (menu + "\n\n");
					opc2 = this.retornaInteiro(entrada);
					switch (opc2){
					case 1: automoveis.add((Automovel)leCarro());
					break;
					case 2: automoveis.add((Automovel)leMoto());
					break;
					case 3: automoveis.add((Automovel)leOnibus());
					break;
					default: 
						JOptionPane.showMessageDialog(null,"Automovel para entrada NÃO escolhido!");
					}
					break;
				case 2: 
					if (automoveis.size() == 0) {
						JOptionPane.showMessageDialog(null,"Entre com automoveis primeiramente");
						break;
					}
					String dados = "";
					for (int i=0; i < automoveis.size(); i++)	{
						dados += automoveis.get(i).toString() + "---------------\n";
					}
					JOptionPane.showMessageDialog(null,dados);
					break;
				case 3: 
					if (automoveis.size() == 0) {
						JOptionPane.showMessageDialog(null,"Entre com automoveis primeiramente");
						break;
					}
					automoveis.clear();
					JOptionPane.showMessageDialog(null,"Dados LIMPOS com sucesso!");
					break;
				case 4: 
					if (automoveis.size() == 0) {
						JOptionPane.showMessageDialog(null,"Entre com automoveis primeiramente");
						break;
					}
					salvaAutomoveis(automoveis);
					JOptionPane.showMessageDialog(null,"Dados SALVOS com sucesso!");
					break;
				case 5: 
					automoveis = recuperaAutomoveis();
					if (automoveis.size() == 0) {
						JOptionPane.showMessageDialog(null,"Sem dados para apresentar.");
						break;
					}
					JOptionPane.showMessageDialog(null,"Dados RECUPERADOS com sucesso!");
					break;
				case 6:
					JOptionPane.showMessageDialog(null,"Fim do aplicativo CONCESSIONARIA");
					break;
				}
			} while (opc1 != 6);
		}
		public static void main (String [] args){

			Concessionaria conc = new Concessionaria ();
			conc.menuConcessionaria();
		}
 }