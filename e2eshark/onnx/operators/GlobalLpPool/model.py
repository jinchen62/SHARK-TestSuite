# Copyright 2024 Advanced Micro Devices, Inc.
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

# run.py creates runmodel.py by concatenating this file model.py
# and tools/stubs/onnxmodel.py
# Description: testing GlobalLpPool
# See https://onnx.ai/onnx/intro/python.html for intro on creating
# onnx model using python onnx API
from commonutils import E2ESHARK_CHECK_DEF
import numpy
import torch
import sys
import onnxruntime
from onnx import TensorProto
from onnx.helper import (
    make_model,
    make_node,
    make_graph,
    make_tensor_value_info,
)

# import from e2eshark/tools to allow running in current dir, for run through
# run.pl, commutils is symbolically linked to allow any rundir to work
sys.path.insert(0, "../../../tools/stubs")

# Create an instance of it for this test
E2ESHARK_CHECK = dict(E2ESHARK_CHECK_DEF)

# TEST(1) : default p value 2D Case
# Create an input (ValueInfoProto)
X = make_tensor_value_info("X", TensorProto.FLOAT, [1, 1, 5, 5])

# Create an output
Y = make_tensor_value_info("Y", TensorProto.FLOAT, [1, 1, 1, 1])

# Create a node (NodeProto)
lppool_node = make_node(
    op_type="GlobalLpPool",
    inputs=["X"],
    outputs=["Y"],
    name="global_lp_pool",
)

# Create the graph (GraphProto)
graph = make_graph(
    nodes=[lppool_node],
    name="global_lp_pool_graph",
    inputs=[X],
    outputs=[Y],
)

# Create the model (ModelProto)
onnx_model = make_model(graph)
onnx_model.opset_import[0].version = 19

# Save the model
with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

session = onnxruntime.InferenceSession("model.onnx", None)
model_input_X = numpy.random.randn(1, 1, 5, 5).astype(numpy.float32)
inputs = session.get_inputs()
outputs = session.get_outputs()

model_output = session.run(
    [outputs[0].name],
    {inputs[0].name: model_input_X},
)

print("Input shape:", model_input_X.shape)
print("Output shape:", numpy.array(model_output[0]).shape)

# Moving to torch to handle bfloat16 as numpy does not support bfloat16
E2ESHARK_CHECK["input"] = [torch.from_numpy(model_input_X)]
E2ESHARK_CHECK["output"] = [torch.from_numpy(arr) for arr in model_output]

print("Input:", E2ESHARK_CHECK["input"])
print("Output:", E2ESHARK_CHECK["output"])

# TEST(2) : Non-Default p value 2D case
# Create an input (ValueInfoProto)
X = make_tensor_value_info("X", TensorProto.FLOAT, [1, 1, 5, 5])

# Create an output
Y = make_tensor_value_info("Y", TensorProto.FLOAT, [1, 1, 1, 1])

# Create a node (NodeProto)
lppool_node = make_node(
    op_type="GlobalLpPool",
    inputs=["X"],
    outputs=["Y"],
    name="global_lp_pool",
    p=3
)

# Create the graph (GraphProto)
graph = make_graph(
    nodes=[lppool_node],
    name="global_lp_pool_graph",
    inputs=[X],
    outputs=[Y],
)

# Create the model (ModelProto)
onnx_model = make_model(graph)
onnx_model.opset_import[0].version = 19

# Save the model
with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

session = onnxruntime.InferenceSession("model.onnx", None)
model_input_X = numpy.random.randn(1, 1, 5, 5).astype(numpy.float32)
inputs = session.get_inputs()
outputs = session.get_outputs()

model_output = session.run(
    [outputs[0].name],
    {inputs[0].name: model_input_X},
)

print("Input shape:", model_input_X.shape)
print("Output shape:", numpy.array(model_output[0]).shape)

# Moving to torch to handle bfloat16 as numpy does not support bfloat16
E2ESHARK_CHECK["input"] = [torch.from_numpy(model_input_X)]
E2ESHARK_CHECK["output"] = [torch.from_numpy(arr) for arr in model_output]

print("Input:", E2ESHARK_CHECK["input"])
print("Output:", E2ESHARK_CHECK["output"])

# TEST(3) : 1D Case, Non default p value
# Create an input (ValueInfoProto)
X = make_tensor_value_info("X", TensorProto.FLOAT, [1, 1, 5])

# Create an output
Y = make_tensor_value_info("Y", TensorProto.FLOAT, [1, 1, 1])

# Create a node (NodeProto)
lppool_node = make_node(
    op_type="GlobalLpPool",
    inputs=["X"],
    outputs=["Y"],
    name="global_lp_pool",
    p=3
)

# Create the graph (GraphProto)
graph = make_graph(
    nodes=[lppool_node],
    name="global_lp_pool_graph",
    inputs=[X],
    outputs=[Y],
)

# Create the model (ModelProto)
onnx_model = make_model(graph)
onnx_model.opset_import[0].version = 19

# Save the model
with open("model.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

session = onnxruntime.InferenceSession("model.onnx", None)
model_input_X = numpy.random.randn(1, 1, 5).astype(numpy.float32)
inputs = session.get_inputs()
outputs = session.get_outputs()

model_output = session.run(
    [outputs[0].name],
    {inputs[0].name: model_input_X},
)

print("Input shape:", model_input_X.shape)
print("Output shape:", numpy.array(model_output[0]).shape)

# Moving to torch to handle bfloat16 as numpy does not support bfloat16
E2ESHARK_CHECK["input"] = [torch.from_numpy(model_input_X)]
E2ESHARK_CHECK["output"] = [torch.from_numpy(arr) for arr in model_output]

print("Input:", E2ESHARK_CHECK["input"])
print("Output:", E2ESHARK_CHECK["output"])
