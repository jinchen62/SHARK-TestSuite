module {
  func.func @test_dequantizelinear_e4m3fn_float16(%arg0: !torch.vtensor<[5],f8E4M3FN>, %arg1: !torch.vtensor<[],f16>) -> !torch.vtensor<[5],f16> attributes {torch.onnx_meta.ir_version = 10 : si64, torch.onnx_meta.opset_version = 21 : si64, torch.onnx_meta.producer_name = "backend-test", torch.onnx_meta.producer_version = ""} {
    %none = torch.constant.none
    %0 = torch.operator "onnx.DequantizeLinear"(%arg0, %arg1) {torch.onnx.axis = 0 : si64} : (!torch.vtensor<[5],f8E4M3FN>, !torch.vtensor<[],f16>) -> !torch.vtensor<[5],f16> 
    return %0 : !torch.vtensor<[5],f16>
  }
}

