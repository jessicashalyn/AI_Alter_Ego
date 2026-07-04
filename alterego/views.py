import os
import io
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from dotenv import load_dotenv
from groq import Groq
from reportlab.pdfgen import canvas

# ======================================
# Load Environment Variables
# ======================================

load_dotenv()
print("=" * 50)
print("GROQ API KEY:")
print(os.getenv("GROQ_API_KEY"))
print("=" * 50)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ======================================
# Home Page
# ======================================

def home(request):
    return render(request, "index.html")


# ======================================
# Generate AI Alter Ego
# ======================================

@csrf_exempt
def generate(request):

    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "error": "POST request required."
        })

    try:

        data = json.loads(request.body)

        name = data.get("name", "").strip()
        hobby = data.get("hobby", "").strip()

        if not name or not hobby:
            return JsonResponse({
                "success": False,
                "error": "Please enter Name and Hobby."
            })

        prompt = f"""
You are a creative AI superhero creator.

Create a fun, exciting and unique superhero alter ego.

Name: {name}
Hobby: {hobby}

IMPORTANT RULES

- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- Do NOT explain anything.
- strengths must always be a JSON array.

Choose avatar ONLY from:
🦸 🦸‍♀️ 🥷 🧙 🤖 🐉 🦅 🦁 🐺 ⚡

Return EXACTLY this JSON:

{{
    "secret_identity":"",
    "avatar":"",
    "strengths":[
        "",
        "",
        ""
    ],
    "power":"",
    "enemy":"",
    "catchphrase":"",
    "weakness":"",
    "mission":""
}}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            response_format={
                "type": "json_object"
            },
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": "You ALWAYS return ONLY valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        output = response.choices[0].message.content.strip()

        output = (
            output
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        try:
            parsed = json.loads(output)

        except json.JSONDecodeError:

            return JsonResponse({
                "success": False,
                "error": "AI returned invalid JSON.",
                "raw_output": output
            })

        return JsonResponse({
            "success": True,
            "output": parsed
        })

    except Exception as e:

        return JsonResponse({
            "success": False,
            "error": str(e)
        })


# ======================================
# Download PDF
# ======================================

@csrf_exempt
def download_pdf(request):

    if request.method != "POST":
        return HttpResponse(status=405)

    try:

        data = json.loads(request.body)

        buffer = io.BytesIO()

        pdf = canvas.Canvas(buffer)

        pdf.setTitle("AI Alter Ego")

        pdf.setFont("Helvetica-Bold", 22)
        pdf.drawString(60, 800, "AI ALTER EGO")

        y = 760

        sections = [

            ("Secret Identity", data["secret_identity"]),

            ("Avatar", data["avatar"]),

            ("Power", data["power"]),

            ("Enemy", data["enemy"]),

            ("Catchphrase", data["catchphrase"]),

            ("Weakness", data["weakness"]),

            ("Mission", data["mission"])

        ]

        pdf.setFont("Helvetica-Bold", 16)

        pdf.drawString(60, y, "Strengths")

        y -= 25

        pdf.setFont("Helvetica", 14)

        for strength in data["strengths"]:

            pdf.drawString(80, y, "• " + strength)

            y -= 22

        y -= 20

        for title, value in sections:

            pdf.setFont("Helvetica-Bold", 16)

            pdf.drawString(60, y, title)

            y -= 25

            pdf.setFont("Helvetica", 14)

            pdf.drawString(80, y, str(value))

            y -= 40

        pdf.save()

        buffer.seek(0)

        response = HttpResponse(
            buffer,
            content_type="application/pdf"
        )

        response["Content-Disposition"] = 'attachment; filename="AI_Alter_Ego.pdf"'

        return response

    except Exception as e:

        return JsonResponse({
            "success": False,
            "error": str(e)
        })