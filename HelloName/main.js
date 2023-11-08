const readline = require ('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (nome) => {
    const saudacao = `Olá, ${nome}`;
    console.log(saudacao);
    rl.close();
});