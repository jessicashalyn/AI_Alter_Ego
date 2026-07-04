const btn = document.getElementById("generateBtn");
const loading = document.getElementById("loading");
const result = document.getElementById("result");

const copyBtn = document.getElementById("copyBtn");
const resetBtn = document.getElementById("resetBtn");
const downloadBtn = document.getElementById("downloadBtn");

let currentAlterEgo = null;


// =========================
// GENERATE
// =========================

btn.onclick = async () => {

    const name = document.getElementById("name").value.trim();
    const hobby = document.getElementById("hobby").value.trim();

    if (name === "" || hobby === "") {
        alert("Please enter all fields.");
        return;
    }

    loading.style.display = "block";
    result.style.display = "none";
    result.innerHTML = "";

    try {

        const response = await fetch("/generate/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                hobby: hobby
            })

        });

        const data = await response.json();

        loading.style.display = "none";

        if (!data.success) {
            alert(data.error);
            return;
        }

        const ego = data.output;

        currentAlterEgo = ego;

        const colors = [
            "#7c3aed",
            "#2563eb",
            "#059669",
            "#dc2626",
            "#db2777",
            "#ea580c",
            "#0891b2"
        ];

        const randomColor = colors[Math.floor(Math.random() * colors.length)];

        result.innerHTML = `

        <div class="card" style="border-top:8px solid ${randomColor};">

            <div class="avatar">

                ${ego.avatar}

            </div>

            <h2>${ego.secret_identity}</h2>

            <hr>

            <h3>⚡ Power</h3>

            <p>${ego.power}</p>

            <h3>💪 Strengths</h3>

            <ul>

                ${ego.strengths.map(item => `<li>${item}</li>`).join("")}

            </ul>

            <h3>👿 Enemy</h3>

            <p>${ego.enemy}</p>

            <h3>🔥 Catchphrase</h3>

            <p>${ego.catchphrase}</p>

            <h3>⚠ Weakness</h3>

            <p>${ego.weakness}</p>

            <h3>🌍 Mission</h3>

            <p>${ego.mission}</p>

        </div>

        `;

        result.style.display = "block";

    }

    catch (err) {

        loading.style.display = "none";

        console.log(err);

        alert("Connection Error");

    }

};


// =========================
// COPY
// =========================

copyBtn.onclick = async () => {

    if (!currentAlterEgo) {

        alert("Generate an Alter Ego first!");

        return;

    }

    const text = `

🦸 SECRET IDENTITY
${currentAlterEgo.secret_identity}

${currentAlterEgo.avatar}

⚡ POWER
${currentAlterEgo.power}

💪 STRENGTHS
${currentAlterEgo.strengths.join("\n")}

👿 ENEMY
${currentAlterEgo.enemy}

🔥 CATCHPHRASE
${currentAlterEgo.catchphrase}

⚠ WEAKNESS
${currentAlterEgo.weakness}

🌍 MISSION
${currentAlterEgo.mission}

`;

    try {

        await navigator.clipboard.writeText(text);

        alert("✅ Copied Successfully!");

    }

    catch {

        alert("Copy Failed!");

    }

};


// =========================
// RESET
// =========================

resetBtn.onclick = () => {

    document.getElementById("name").value = "";
    document.getElementById("hobby").value = "";

    result.innerHTML = "";

    result.style.display = "none";

    loading.style.display = "none";

    currentAlterEgo = null;

};


// =========================
// DOWNLOAD PDF
// =========================

downloadBtn.onclick = async () => {

    if (!currentAlterEgo) {

        alert("Generate an Alter Ego first!");

        return;

    }

    try {

        const response = await fetch("/download-pdf/", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify(currentAlterEgo)

        });

        if (!response.ok) {

            throw new Error();

        }

        const blob = await response.blob();

        const url = window.URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = url;

        a.download = "AI_Alter_Ego.pdf";

        document.body.appendChild(a);

        a.click();

        a.remove();

        window.URL.revokeObjectURL(url);

    }

    catch (err) {

        console.log(err);

        alert("Unable to download PDF.");

    }

};