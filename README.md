# V2X-Sim-mini Creator

Code in this repository creates a mini dataset from a given scene in [V2X-Sim dataset](https://ai4ce.github.io/V2X-Sim/) \
Metadata will be extracted, and sensor data will be copied.  

## Usage
1. Clone this repository.
2. Place this repository parallel to where your `V2X-Sim` dataset is.
3. `cd` into this repository.

```bash
make create --scene=$(SCENE_NUMBER)
```

You might need to look into the code and have necessary modifications, since this repo was intended to be for one-time use only, without considering much about generalization.