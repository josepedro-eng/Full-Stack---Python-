console.log("script.js carregado");

const API = "http://127.0.0.1:8000";


// ======================
// BOTÕES
// ======================

document.addEventListener("DOMContentLoaded", () => {

    document
        .getElementById("btnCriarUsuario")
        .addEventListener("click", criarUsuario);

    document
        .getElementById("btnCriarTarefa")
        .addEventListener("click", criarTarefa);

    listarUsuarios();

});



// ======================
// LISTAR USUÁRIOS
// ======================

async function listarUsuarios() {

    try {

        const resposta =
            await fetch(`${API}/usuarios/`);

        const usuarios =
            await resposta.json();

        const lista =
            document.getElementById("listaUsuarios");

        lista.innerHTML = "";

        usuarios.forEach(usuario => {

            const item =
                document.createElement("li");

            item.innerText =
                `ID: ${usuario.id} - ${usuario.nome}`;

            const botao =
                document.createElement("button");

            botao.innerText =
                "Ver tarefas";

            botao.onclick = () => {
                listarTarefas(usuario.id);
            };

            item.appendChild(botao);

            lista.appendChild(item);

        });

    }

    catch (erro) {

        console.error(
            "Erro ao listar usuários:",
            erro
        );

    }

}



// ======================
// CRIAR USUÁRIO
// ======================

async function criarUsuario() {

    const nome =
        document.getElementById("nome").value;

    const email =
        document.getElementById("email").value;

    try {

        await fetch(`${API}/usuarios/`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                nome: nome,
                email: email
            })

        });

        listarUsuarios();

    }

    catch (erro) {

        console.error(
            "Erro ao criar usuário:",
            erro
        );

    }

}



// ======================
// CRIAR TAREFA
// ======================

async function criarTarefa() {

    const titulo =
        document.getElementById("tituloTarefa").value;

    const descricao =
        document.getElementById("descricaoTarefa").value;

    const usuario_id =
        document.getElementById("usuarioIdTarefa").value;

    try {

        await fetch(`${API}/tarefas/`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                titulo: titulo,
                descricao: descricao,
                usuario_id: Number(usuario_id)

            })

        });

        listarTarefas(usuario_id);

    }

    catch (erro) {

        console.error(
            "Erro ao criar tarefa:",
            erro
        );

    }

}



// ======================
// LISTAR TAREFAS
// ======================

async function listarTarefas(usuario_id) {

    try {

        const resposta =
            await fetch(
                `${API}/usuarios/${usuario_id}/tarefas`
            );

        const tarefas =
            await resposta.json();

        const lista =
            document.getElementById("listaTarefas");

        lista.innerHTML = "";

        tarefas.forEach(tarefa => {

            const item =
                document.createElement("li");

            item.innerText =
                `${tarefa.titulo} - ${tarefa.descricao}`;

            lista.appendChild(item);

        });

    }

    catch (erro) {

        console.error(
            "Erro ao listar tarefas:",
            erro
        );

    }

}