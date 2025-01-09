export CACHE_DIR=/proj/gdba/shark/jinchen/cache/

source /proj/gdba/shark/jinchen/iree-build/.env && export PYTHONPATH

export PYTHONPATH=/proj/gdba/shark/jinchen/torch-mlir/build/tools/torch-mlir/python_packages/torch_mlir:/proj/gdba/shark/jinchen/torch-mlir/test/python/fx_importer:$PYTHONPATH

export PATH=/proj/gdba/shark/jinchen/iree-build/tools/:/proj/gdba/shark/jinchen/torch-mlir/build/bin/:$PATH

export HF_HOME=/proj/gdba/shark/jinchen/cache/huggingface/

export HF_TOKEN=""

python ./run.py --mode=cl-onnx-iree -v --torchtolinalg --testsfile list_tmp.txt
