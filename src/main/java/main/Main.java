package main;

import vn.hus.nlp.tokenizer.VietTokenizer;

public class Main {

    public static void main(String[] args) {
        Main runner = new Main();
        runner.run();
    }

    private void run() {
        VietTokenizer tokenizer = new VietTokenizer();
        tokenizer.tokenize(
                "test/1.txt",
                "test/1.out.txt"
        );
    }
}