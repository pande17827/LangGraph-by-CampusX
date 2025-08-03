from manim import *

class TweetWorkflow(Scene):
    def construct(self):
        # Ultra minimal colors
        self.camera.background_color = "#000000"
        
        # Simple positions - straight vertical line
        y_positions = [3, 1.5, 0, -1.5, -3, -4.5]
        
        # Simple white boxes
        boxes = []
        texts = []
        
        # Just text in boxes, nothing fancy
        labels = [
            "START",
            "GENERATOR\nGemini Pro",
            "EVALUATOR\nGemini Flash", 
            "APPROVED?",
            "OPTIMIZER\nGemini 2.0",
            "END"
        ]
        
        for i, (y_pos, label) in enumerate(zip(y_positions, labels)):
            # Simple white rectangle
            box = Rectangle(
                width=3, height=0.8,
                color=WHITE,
                fill_opacity=0.1,
                stroke_width=1
            ).shift(UP * y_pos)
            
            # Simple white text
            text = Text(label, color=WHITE, font_size=16).move_to(box)
            
            boxes.append(box)
            texts.append(text)
        
        # Simple arrows - just lines
        arrows = []
        
        # Straight down arrows
        for i in range(len(y_positions)-2):
            arrow = Arrow(
                [0, y_positions[i] - 0.4, 0],
                [0, y_positions[i+1] + 0.4, 0],
                color=WHITE,
                stroke_width=1,
                tip_length=0.1
            )
            arrows.append(arrow)
        
        # Decision arrows
        # To end
        end_arrow = Arrow(
            [-0.5, y_positions[3] - 0.4, 0],
            [-0.5, y_positions[5] + 0.4, 0],
            color=WHITE,
            stroke_width=1,
            tip_length=0.1
        )
        
        # To optimizer
        opt_arrow = Arrow(
            [0.5, y_positions[3] - 0.4, 0],
            [0.5, y_positions[4] + 0.4, 0],
            color=WHITE,
            stroke_width=1,
            tip_length=0.1
        )
        
        # Loop back
        loop_line = Line(
            [0.8, y_positions[4], 0],
            [0.8, y_positions[2], 0],
            color=WHITE,
            stroke_width=1
        )
        loop_arrow = Arrow(
            [0.8, y_positions[2], 0],
            [0.4, y_positions[2], 0],
            color=WHITE,
            stroke_width=1,
            tip_length=0.1
        )
        
        # Simple labels
        yes_label = Text("YES", color=WHITE, font_size=12).shift(LEFT * 1 + DOWN * 2.7)
        no_label = Text("NO", color=WHITE, font_size=12).shift(RIGHT * 1 + DOWN * 2.2)
        
        # Show everything at once - no fancy animation
        self.add(*boxes)
        self.add(*texts)
        self.add(*arrows)
        self.add(end_arrow, opt_arrow)
        self.add(loop_line, loop_arrow)
        self.add(yes_label, no_label)
        
        self.wait(3)