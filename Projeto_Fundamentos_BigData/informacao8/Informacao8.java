/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pucpr.atp.projetohadoop;

import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
// 8 Mercadoria com maior peso total em todas as transacoes 
//Indice
//0 país
//1 ano
//2 codigo
//3 comodite
//4 flow
//5 valor dol
//6 peso
//7 quantidade nome
//8 quantidade
//9 categoria
/**
 *
 * @author estevan.rafael
 */

public class Informacao8 {

    public static class Mapper8 extends Mapper<Object, Text, Text, LongWritable> {

        @Override
        public void map(Object chave, Text valor, Context context) throws IOException, InterruptedException {
            try {
                
                String[] campo = valor.toString().split(";");
                if (campo.length == 10) {
                   
                    Text chaveCampo = new Text(campo[1] + "-" + campo[3]);
                    LongWritable valorMapa = new LongWritable(Long.parseLong(campo[6]));

                    context.write(chaveCampo, valorMapa);

                }
            } catch (IOException | InterruptedException | NumberFormatException err) {
                System.out.println(err);
            }

        }

    }

    public static class Reducer8 extends Reducer<Text, LongWritable, Text, LongWritable> {

        @Override
        public void reduce(Text chave, Iterable<LongWritable> valores, Context context) throws IOException, InterruptedException {
            long i = 0;

            for (LongWritable val : valores) {
                i += val.get();
            }

            context.write(chave, new LongWritable(i));

        }

    }

    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {

        String entrada = "/home/Disciplinas/FundamentosBigData/OperacoesComerciais/base_100_mil.csv";
        //String entrada = "/home/Disciplinas/FundamentosBigData/OperacoesComerciais/base_inteira.csv";
        String saida = "/home2/ead2021/SEM1/estevan.rafael/Desktop/atp/" + Informacao8.class.getSimpleName();
        //String saida = "/home2/ead2021/SEM1/estevan.rafael/Desktop/atp/" + Informacao8.class.getSimpleName();

        if (args.length == 2) {
            saida = args[0];
            entrada = args[1];
        }

        Configuration config = new Configuration();
        Job job = Job.getInstance(config, Informacao8.class.getSimpleName());

        job.setJarByClass(Informacao8.class);
        job.setMapperClass(Mapper8.class);
        job.setReducerClass(Reducer8.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        FileInputFormat.addInputPath(job, new Path(entrada));
        FileOutputFormat.setOutputPath(job, new Path(saida));

        job.waitForCompletion(true);
    }
    
}
