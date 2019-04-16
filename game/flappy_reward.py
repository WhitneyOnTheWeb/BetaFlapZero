def draw_polygons(self, pipes, gaps):
        BLACK = (0, 0, 0)
        danger = []
        # upper left of pipe[0]
        a = (0, 0)
        b = (pipes['upper'][0]['x'], 0)
        c = (pipes['upper'][0]['x'], gaps[0]['y'])
        d = (0, gaps[0]['y'])
        danger.append([a, b, c, d])
        # lower left of pipe[0]
        a = (0, pipes['lower'][0]['y'])
        b = (pipes['lower'][0]['x'], pipes['lower'][0]['y'])
        c = (pipes['lower'][0]['x'], BASE_Y)
        d = (0, BASE_Y)
        danger.append([a, b, c, d])
        #between upper pipe[0] and pipe[1]
        a = (pipes['upper'][0]['x'] + PIPE_W, 0)
        b = (pipes['upper'][1]['x'], 0)
        c = (pipes['upper'][1]['x'], gaps[1]['y'])
        d = (pipes['upper'][0]['x']  + PIPE_W, gaps[0]['y'])
        danger.append([a, b, c, d])

        a = (pipes['lower'][0]['x'] + PIPE_W, pipes['lower'][0]['y'])
        b = (pipes['lower'][1]['x'], pipes['lower'][1]['y'])
        c = (pipes['lower'][1]['x'], BASE_Y)
        d = (pipes['lower'][0]['x'] + PIPE_W, BASE_Y)
        danger.append([a, b, c, d])

        a = (pipes['upper'][1]['x'] + PIPE_W, 0)
        b = (SCREEN_W, 0)
        c = (SCREEN_W, gaps[1]['y'])
        d = (pipes['upper'][1]['x'] + PIPE_W, gaps[1]['y'])
        danger.append([a, b, c, d])
        
        a = (pipes['lower'][1]['x'] + PIPE_W, pipes['lower'][1]['y'])
        b = (SCREEN_W, pipes['lower'][1]['y'])
        c = (SCREEN_W, BASE_Y)
        d = (pipes['lower'][1]['x'] + PIPE_W, BASE_Y)
        danger.append([a, b, c, d])

        danger_zone = []
        masks = []
        for z in danger:
            poly = [z[0], z[1], z[2], z[3]]
            danger_zone.append(pygame.draw.polygon(SCREEN, BLACK, poly))
            masks.append(fl.getHitmask(poly))
        return danger_zone, masks