// static/js/api.js

export async function postData(endpoint, data) {
  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    // Verifica si la respuesta es correcta
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    // Devuelve la respuesta como JSON
    return await response.json();
  } catch (error) {
    console.error("Error en la solicitud:", error);
    return { success: false, error: error.message };
  }
}
