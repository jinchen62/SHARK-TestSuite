module {
  func.func @test_bitshift_right_uint32(%arg0: !torch.vtensor<[3],ui32>, %arg1: !torch.vtensor<[3],ui32>) -> !torch.vtensor<[3],ui32> attributes {torch.onnx_meta.ir_version = 6 : si64, torch.onnx_meta.opset_version = 11 : si64, torch.onnx_meta.producer_name = "backend-test", torch.onnx_meta.producer_version = ""} {
    %0 = torch.operator "onnx.BitShift"(%arg0, %arg1) {torch.onnx.direction = "RIGHT"} : (!torch.vtensor<[3],ui32>, !torch.vtensor<[3],ui32>) -> !torch.vtensor<[3],ui32>
    return %0 : !torch.vtensor<[3],ui32>
  }
}
