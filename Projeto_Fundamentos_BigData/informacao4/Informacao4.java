/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.pucpr.atp.projetohadoop;

import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
// 4 Mercadoria com maior transacao em dol
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
public class Informacao4 {

    public static class Mapper4 extends Mapper<Object, Text, Text, IntWritable> {

        @Override
        public void map(Object chave, Text valor, Context context) throws IOException, InterruptedException {
            try {
                
                String[] campo = value.toString().split(";");
                if (campo.length == 10) {
                   
                    Text chaveCampo = new Text(campo[3]);
                    IntWritable valorMapa = new IntWritable(1);

                    context.write(chaveCampo, valorMapa);

                }
            } catch (IOException | InterruptedException | NumberFormatException err) {
                System.out.println(err);
            }

        }

    }

    public static class Reducer4 extends Reducer<Text, IntWritable, Text, IntWritable> {

        @Override
        public void reduce(Text chave, Iterable<IntWritable> valores, Context context) throws IOException, InterruptedException {
            int i = 0;

            for (IntWritable val : valores) {
                i += val.get();
            }

            context.write(chave, new IntWritable(i));

        }

    }

    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException {

        String entrada = "/home/Disciplinas/FundamentosBigData/OperacoesComerciais/base_100_mil.csv";
        //String entrada = "/home/Disciplinas/FundamentosBigData/OperacoesComerciais/base_inteira.csv";
        String saida = "/home2/ead2021/SEM1/estevan.rafael/Desktop/atp/" + Informacao4.class.getSimpleName();
        //String saida = "/home2/ead2021/SEM1/estevan.rafael/Desktop/atp/" + Informacao4.class.getSimpleName();

        if (args.length == 2) {
            saida = args[0];
            entrada = args[1];
        }

        Configuration config = new Configuration();
        Job job = Job.getInstance(config, Informacao4.class.getSimpleName());

        job.setJarByClass(Informacao4.class);
        job.setMapperClass(Mapper4.class);
        job.setReducerClass(Reducer4.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(entrada));
        FileOutputFormat.setOutputPath(job, new Path(saida));

        job.waitForCompletion(true);
    }
    
}
