import ruldani_visual_programming.color_manager as cm


# warna node
default = cm.GRAY_PALLETE
path = cm.RED_PALLETE
plt = cm.RED_PALLETE
output = cm.CYAN_PALLETE


# Kelas untuk membuat berzier curve
class nodeberzier:

    # inisialisasi node berzier
    def __init__(self, canvas, node_type, image_id, coor, nodeberzier_container, active_line):
        self.canvas = canvas
        self.radius = 5
        self.type = node_type  # Store node type
        self.image_id = image_id  # Store the image_id reference
        self.coor = coor

        # Bezier curve related attributes
        self.line_id = None
        self.next = None
        
        # Get the current position of the image from canvas
        # Bind events for the node
        self.image_id.bind('<Button-1>', self.start_connection)
        self.image_id.bind('<B1-Motion>', self.on_drag)
        self.image_id.bind('<ButtonRelease-1>', self.on_release)
        self.connection_line = None
        self.node_next = None
        self.nodeberzier_container = nodeberzier_container
        self.active_line = active_line
    
    def line_colour(self):
        if self.type == "path":
            return path
        
        return default

    def start_connection(self, event): 
  
        self.canvas.delete(self.line_id)
        if self.next != None :
            self.next.line_id = None
            self.next.next = None
            self.next.canvas.delete(self.next.line_id)
        self.line_id = None
        self.next = None
        self.active_line = self
        self.x = self.image_id.winfo_x() + self.coor.winfo_x()
        self.y = self.image_id.winfo_y() + self.coor.winfo_y() + 5
    
    def on_drag(self, event): 
        x = event.x + self.x
        y = event.y + self.y
        if self.active_line:
            self.update_curve(self.x, self.y, x, y -5)
    
    def on_release(self, event): 
        
        self.connection_line = None
        for node in self.nodeberzier_container:
            if node.coor != self.coor:
                x = event.x + self.x
                y = event.y + self.y
                node_x = node.image_id.winfo_x() + node.coor.winfo_x()  
                node_y = node.image_id.winfo_y() + node.coor.winfo_y()

                if ( abs(x - node_x) < 7 and -7 < abs(y -10 - node_y) < 7 ): 
                    if (self.type == node.type):
                        
                        if node.next != None : 
                            node.canvas.delete(node.line_id)
                            node.next.next = None
                            node.next = None

                        if self.next != None :
                            self.canvas.delete(self.line_id)
                            self.next = None
                            
                        self.update_curve(self.x, self.y, node_x, node_y+5)
                        self.connection_line = self.line_id
                        node.connection_line = self.line_id
                        node.line_id = self.line_id
                        node.next = self
                        self.next = node
                        self.active_line = None
                        break
        
        if not self.connection_line :
            self.canvas.delete(self.line_id)
            active_line = None
            self.line_id = None

    def update_curve(self, x1, y1, x2, y2):
        # Update the coordinates for the curve
        self.canvas.delete(self.line_id)
        cx1, cy1 = (x1 + x2) / 2, y1
        cx2, cy2 = (x1 + x2) / 2, y2
        points = self.bezier_points(x1, y1, cx1, cy1, cx2, cy2, x2, y2)
        self.line_id = self.canvas.create_line(points, fill=self.line_colour(), width=2, tags="line", smooth=True)

    def bezier_points(self, x1, y1, cx1, cy1, cx2, cy2, x2, y2, num_points=100):
        points = []
        for t in range(num_points + 1):
            t /= num_points
            x = (1 - t) ** 3 * x1 + 3 * (1 - t) ** 2 * t * cx1 + 3 * (1 - t) * t ** 2 * cx2 + t ** 3 * x2
            y = (1 - t) ** 3 * y1 + 3 * (1 - t) ** 2 * t * cy1 + 3 * (1 - t) * t ** 2 * cy2 + t ** 3 * y2
            points.append((x, y))
        return points
    
    def force_update(self):
        
        self.canvas.delete(self.line_id)
        self.line_id = None
        if self.next != None :

            node = self.next
            node_x = node.image_id.winfo_x() + node.coor.winfo_x()
            node_y = node.image_id.winfo_y() + node.coor.winfo_y()+5
            x = self.image_id.winfo_x() + self.coor.winfo_x()
            y = self.image_id.winfo_y() + self.coor.winfo_y()+5
            self.update_curve(x,y,node_x,node_y)
            node.line_id = self.line_id

    
    def delete_line(self):
        if self.line_id != None :
            self.canvas.delete(self.line_id)
            self.line_id = None
            self.next.line_id = None
            self.next.next = None
        self.nodeberzier_container.remove(self)
