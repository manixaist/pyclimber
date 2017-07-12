"""Particle generator for Py-Climber"""
from src.particle import Particle
import random

class ParticleGenerator():
    """The ParticleGenerator class is responsible for creating and tracking Particle
    objects which are just 2D rects of a given color.  A calling object may specify
    a callback to customize the particles generated, e.g. their velocities and color
    """

    def __init__(self, screen, settings, color, x, y, generator_callback=None):
        """Init the position and color"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.x = x
        self.y = y
        self.color = color
        self.particles = []
        self.active = False
        self.active_frames = 0
        self.frames_to_generate = 0
        self.callback = generator_callback

    def start(self, frames_to_generate):
        """Tells the generator to start generating particles"""
        self.active = True
        self.active_frames = 0
        self.frames_to_generate = frames_to_generate

    def stop(self):
        """Tells the generator to stop generating particles"""
        self.active = False
        self.active_frames = 0
        # start() dictates the duration
        self.frames_to_generate = 0

    def update(self):
        """Update the position of all alive particles"""
        # We always want to draw the particles, so unlike other sprites,
        # the 'active' or 'on' property will control the generation instead
        # This way when the generator stops, the existing particles will
        # finish out their lives.  If it controlled the drawing, particles
        # in-flight would just vanish (or you would need additional logic
        # in the drawing code)
        if self.active:
            self.generate_particles(self.settings.particle_gen_per_frame)
            self.active_frames += 1
            if self.active_frames > self.frames_to_generate:
                self.stop()

        # For any particles still alive, we need to update them, even if the 
        # generator is stopped.  Once a particle is 'dead', remove it
        for particle in self.particles:
            particle.update()
            if not particle.alive():
                self.particles.remove(particle)

    def generate_particles(self, number_of_new_particles):
        """Create a new particle at the generator's location and give it an initial velocity"""
        # In the callback case the implementer controls it all, including the number
        # create an empty list to hold the data
        particle_data = []
        if self.callback:
            # We have a callback, so delegate all of the work....
            particle_data = self.callback()
        else:
            # No callback, so make some random ones by default
            for particle_index in range(0, number_of_new_particles):
                new_data = (random.randint(-2, 2), random.randint(5, 20) * -1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
                particle_data.append(new_data)

        # Callback or not, at this point we should have a list of particle data
        for particle_info in particle_data:
            # Create a new particle object
            new_particle = Particle(self.screen, self.settings, self.x, self.y, particle_info[0], particle_info[1], random.randint(1, 4), particle_info[2])
            
            # Add it to the list to track/draw
            self.particles.append(new_particle)

    def draw(self):
        """Draw all of the particles"""
        # Since the are not pygame.sprites, can't just use the Group as with the blobs
        # Just another way to do things
        for particle in self.particles:
            particle.draw()
