import pygame
import math


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing_mode = 'line'  # New variable

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_1:  # Switch to line mode
                    drawing_mode = 'line'
                elif event.key == pygame.K_2:  # Switch to circle mode
                    drawing_mode = 'circle'
                elif event.key == pygame.K_3:  # Switch to eraser mode
                    drawing_mode = 'eraser'
                elif event.key == pygame.K_4:  # Switch to rectangle mode
                    drawing_mode = 'rectangle'
                elif event.key == pygame.K_5:  # Switch to square mode
                    drawing_mode = 'square'
                elif event.key == pygame.K_6:  # Switch to right triangle mode
                    drawing_mode = 'right_triangle'
                elif event.key == pygame.K_7:  # Switch to equilateral triangle mode
                    drawing_mode = 'equilateral_triangle'
                elif event.key == pygame.K_8:  # Switch to rhombus mode
                    drawing_mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)
                  

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        # draw all points
        i = 0
        while i < len(points) - 1:
            if drawing_mode == 'line':
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            elif drawing_mode == 'circle':
                pygame.draw.circle(screen, getColor(mode, i), points[i], radius)
            elif drawing_mode == 'rectangle':
                pygame.draw.rect(screen, getColor(mode, i), pygame.Rect(points[i], (radius * 2, radius * 2)))
            elif drawing_mode == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), points[i], radius)
            elif drawing_mode == 'triangle':
                if len(points) >= 3:
                    pygame.draw.polygon(screen, getColor(mode, i), points[i:i+3])
                    i += 2  # Skip to the next set of points
            elif drawing_mode == 'square':
                if len(points) >= 2:  # Ensure at least 2 points to form a square
                    x1, y1 = points[i]
                    x2, y2 = points[i + 1]
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(screen, getColor(mode, i), pygame.Rect(x1, y1, side, side))
                    i += 1
            elif drawing_mode == 'right_triangle':
                if len(points) >= 2:  # Ensure at least 2 points to form a right triangle
                    x1, y1 = points[i]
                    x2, y2 = points[i + 1]
                    height = abs(y2 - y1)
                    base = abs(x2 - x1)
                    pygame.draw.polygon(screen, getColor(mode, i), [(x1, y1), (x1, y1 + height), (x1 + base, y1 + height)])
                    i += 1
            elif drawing_mode == 'equilateral_triangle':
                if len(points) >= 2:  # Ensure at least 2 points to form an equilateral triangle
                    x1, y1 = points[i]
                    x2, y2 = points[i + 1]
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    height = math.sqrt(3) * side / 2
                    pygame.draw.polygon(screen, getColor(mode, i), [(x1, y1), (x1 + side, y1), (x1 + side / 2, y1 - height)])
                    i += 1
            elif drawing_mode == 'rhombus':
                if len(points) >= 2:  # Ensure at least 2 points to form a rhombus
                    x1, y1 = points[i]
                    x2, y2 = points[i + 1]
                    pygame.draw.polygon(screen, getColor(mode, i), [(x1, y1), (x1 + abs(x2 - x1) / 2, y1 + abs(y2 - y1) / 2),
                                                                    (x2, y2), (x1 + abs(x2 - x1) / 2, y1 - abs(y2 - y1) / 2)])
                    i += 1

            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    color = getColor(color_mode, index)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def getColor(color_mode, index):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    return (0, 0, 0)  # Default color



main()
