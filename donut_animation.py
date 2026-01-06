import math
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_donut(a, b):
    # Screen dimensions
    width, height = 80, 40
    
    # Create buffers
    output = [[' ' for _ in range(width)] for _ in range(height)]
    zbuffer = [[0 for _ in range(width)] for _ in range(height)]
    
    # Donut parameters
    theta_spacing = 0.07
    phi_spacing = 0.02
    
    # Precompute sines and cosines of a and b
    cos_a, sin_a = math.cos(a), math.sin(a)
    cos_b, sin_b = math.cos(b), math.sin(b)
    
    # Draw the donut
    theta = 0
    while theta < 2 * math.pi:
        cos_theta, sin_theta = math.cos(theta), math.sin(theta)
        
        phi = 0
        while phi < 2 * math.pi:
            cos_phi, sin_phi = math.cos(phi), math.sin(phi)
            
            # Calculate circle coordinates (before rotation)
            circle_x = 2 + cos_theta
            circle_y = sin_theta
            
            # 3D rotation
            x = circle_x * (cos_b * cos_phi + sin_a * sin_b * sin_phi) - circle_y * cos_a * sin_b
            y = circle_x * (sin_b * cos_phi - sin_a * cos_b * sin_phi) + circle_y * cos_a * cos_b
            z = 5 + cos_a * circle_x * sin_phi + circle_y * sin_a
            ooz = 1 / z  # One over z (for perspective)
            
            # Project to 2D
            xp = int(width / 2 + 30 * ooz * x)
            yp = int(height / 2 - 15 * ooz * y)
            
            # Calculate luminance
            luminance = cos_phi * cos_theta * sin_b - cos_a * cos_theta * sin_phi - sin_a * sin_theta + cos_b * (cos_a * sin_theta - cos_theta * sin_a * sin_phi)
            
            # Check bounds and depth
            if 0 <= xp < width and 0 <= yp < height and ooz > zbuffer[yp][xp]:
                zbuffer[yp][xp] = ooz
                luminance_index = int(luminance * 8)
                output[yp][xp] = ".,-~:;=!*#$@"[max(0, min(luminance_index, 11))]
            
            phi += phi_spacing
        theta += theta_spacing
    
    # Print the frame
    clear_screen()
    for row in output:
        print(''.join(row))

# Animation loop
a, b = 0, 0
try:
    while True:
        render_donut(a, b)
        a += 0.04
        b += 0.02
        time.sleep(0.03)
except KeyboardInterrupt:
    print("\nAnimation stopped!")