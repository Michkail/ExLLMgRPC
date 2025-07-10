import torch
import base64
import io
from diffusers import StableDiffusionPipeline
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5",
                                               torch_dtype=dtype)
pipe = pipe.to(device)

def generate_image_base64(prompt: str) -> str:
    image: Image.Image = pipe(prompt).images[0]
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    return encoded
