# deeplearningproject


ImagesXrayClassification

Data link: https://drive.google.com/file/d/1pfIAlurfeqFTbirUZ5v_vapIoGPgRiXY/view?usp=sharing

- Workflows
- constants
- config_entity
- artifact_entity
- components
- pipeline
- main

### How to setup:
<br> conda create -n lungs python=3.8 -y
<br> conda activate env
<br> pip install -r requirements_dev.txt
<br> setup AWS CLI
link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

<br> aws configure

<br> AWS_ACCESS_KEY_ID = ***
<br> AWS_SECRET_ACCESS_KEY = ***
<br> AWS_REGION = us-east-1

```bash
conda create -n env
```
```bash
conda activate env
```
```bash
pip install -r requirements.txt
```
```bash
setup AWS CLI
```
```bash
aws configure
```

### BentoML demo repo:
https://github.com/entbappy/bentoml-demo