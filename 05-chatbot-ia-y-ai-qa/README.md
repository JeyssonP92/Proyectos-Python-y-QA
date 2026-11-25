# Chatbot Empresarial con IA (Gemini) y Suite de AI QA Testing

Este proyecto implementa un asistente virtual corporativo basado en contexto controlado (**RAG**) utilizando **Google Gemini 3.5 Flash Lite**, acompañado de una suite independiente de **AI Quality Assurance (LLM Eval)** ejecutada con **Pytest** que genera actas de auditoría automáticas.

## Arquitectura del Proyecto

* **`chatbot_clinica.py`**: Motor conversacional híbrido (menú guiado + lenguaje natural) configurado con instrucciones estrictas de sistema (*System Prompt*), temperatura `0.0` y manejo de reintentos ante saturación de red.
* **`test_chatbot_ai_qa.py`**: Suite automatizada de pruebas de calidad que audita tres pilares críticos de IA:
  1. **Fidelidad Factual:** Verifica extracción exacta de tarifas y horarios desde la base de conocimiento oficial.
  2. **Prevención de Alucinaciones:** Certifica el rechazo controlado ante preguntas fuera del dominio de la clínica.
  3. **Seguridad (*Guardrails*):** Valida resistencia ante ataques de manipulación de instrucciones (*Prompt Injection*).
* **`evidencia_auditoria_ia.md`**: Acta de certificación generada automáticamente tras cada ejecución de Pytest con los prompts enviados y las respuestas auditadas.
* **`.env` & `.gitignore`**: Protección de credenciales mediante variables de entorno locales.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Inteligencia Artificial:** Google GenAI SDK (`gemini-3.5-flash-lite`)
* **Testing & QA Automation:** Pytest
* **Seguridad:** `python-dotenv`|