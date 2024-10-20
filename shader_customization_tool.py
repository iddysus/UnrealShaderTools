
import tkinter as tk
from tkinter import ttk

# Main window setup
root = tk.Tk()
root.title("Shader Customization Tool")
root.geometry("400x400")

# Global shader parameters
shader_parameters = {
    "glossiness": 0.5,
    "roughness": 0.5,
    "metallic": 0.5
}

# Function to update shader parameters
def update_shader(param, value):
    shader_parameters[param] = float(value)
    # Mock-up preview of shader parameters (can be connected to an engine)
    print(f"Updated {param}: {shader_parameters[param]}")

# Slider to adjust glossiness
glossiness_label = ttk.Label(root, text="Glossiness")
glossiness_label.pack(pady=5)
glossiness_slider = ttk.Scale(root, from_=0, to=1, orient="horizontal", command=lambda value: update_shader("glossiness", value))
glossiness_slider.set(shader_parameters["glossiness"])
glossiness_slider.pack(pady=5)

# Slider to adjust roughness
roughness_label = ttk.Label(root, text="Roughness")
roughness_label.pack(pady=5)
roughness_slider = ttk.Scale(root, from_=0, to=1, orient="horizontal", command=lambda value: update_shader("roughness", value))
roughness_slider.set(shader_parameters["roughness"])
roughness_slider.pack(pady=5)

# Slider to adjust metallic property
metallic_label = ttk.Label(root, text="Metallic")
metallic_label.pack(pady=5)
metallic_slider = ttk.Scale(root, from_=0, to=1, orient="horizontal", command=lambda value: update_shader("metallic", value))
metallic_slider.set(shader_parameters["metallic"])
metallic_slider.pack(pady=5)

# Button to export shader settings to a file
def export_shader_settings():
    with open("shader_settings.txt", "w") as file:
        for param, value in shader_parameters.items():
            file.write(f"{param}: {value}
")
    print("Shader settings exported to shader_settings.txt")

export_button = ttk.Button(root, text="Export Shader Settings", command=export_shader_settings)
export_button.pack(pady=20)

# Export GLSL shader code
def export_glsl_shader():
    glsl_code = f"""
    // GLSL shader code
    uniform float glossiness = {shader_parameters['glossiness']};
    uniform float roughness = {shader_parameters['roughness']};
    uniform float metallic = {shader_parameters['metallic']};

    void main() {{
        // Example fragment shader logic
        vec3 baseColor = vec3(1.0, 0.0, 0.0);  // Example base color (red)
        vec3 reflectance = mix(baseColor, vec3(1.0), glossiness);
        vec3 finalColor = mix(reflectance, vec3(0.0), roughness);
        gl_FragColor = vec4(finalColor, 1.0);
    }}
    """
    with open("shader_glsl.glsl", "w") as file:
        file.write(glsl_code)
    print("GLSL shader code exported to shader_glsl.glsl")

glsl_export_button = ttk.Button(root, text="Export GLSL Shader", command=export_glsl_shader)
glsl_export_button.pack(pady=10)

root.mainloop()
