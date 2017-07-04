"""This module implements sprite animations for Py-Climber"""

class Animation():
    """Implements animation logic for sprites, this is really just a list of ints - simple"""

    def __init__(self, frame_sequence, delay):
        """Initialize the animation object"""

        # Sequence of ints that are indicies to the external sprite's image list
        self.animation = frame_sequence
        # Assuming Animation.animate() is called once per frame, this is the number
        # of frames before the current index to the sequence list is updated
        self.frames_per_update = delay
        # counter to track when to update the current fram
        self.frames_delayed = 0
        # Which frame in the sequence (list) are we currently showing
        self.current_frame_index = 0
        
    def get_current_frame(self):
        """Returns the frame to render, e.g. the current frame in the animation sequence"""
        return self.animation[self.current_frame_index]

    def reset(self):
        """Reset internal state"""
        self.current_frame_index = 0
        self.frames_delayed = 0

    def animate(self):
        """Update the current frame if needed, or update internal state, 
        should be called once per frame when animating"""
        if self.frames_delayed > self.frames_per_update:
            self.frames_delayed = 0
            self.current_frame_index += 1
            if self.current_frame_index > len(self.animation) - 1:
                self.current_frame_index = 0
        else:
            self.frames_delayed += 1