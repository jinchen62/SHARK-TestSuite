module {
  func.func @test_softmax_axis_2_expanded(%arg0: !torch.vtensor<[3,4,5],f32>) -> !torch.vtensor<[3,4,5],f32> attributes {torch.onnx_meta.ir_version = 7 : si64, torch.onnx_meta.opset_version = 13 : si64, torch.onnx_meta.producer_name = "backend-test", torch.onnx_meta.producer_version = ""} {
    %0 = torch.vtensor.literal(dense<2> : tensor<1xsi64>) : !torch.vtensor<[1],si64>
    %1 = torch.operator "onnx.ReduceMax"(%arg0) {torch.onnx.axes = [2 : si64], torch.onnx.keepdims = 1 : si64} : (!torch.vtensor<[3,4,5],f32>) -> !torch.vtensor<[3,4,1],f32>
    %2 = torch.operator "onnx.Sub"(%arg0, %1) : (!torch.vtensor<[3,4,5],f32>, !torch.vtensor<[3,4,1],f32>) -> !torch.vtensor<[3,4,5],f32>
    %3 = torch.operator "onnx.Exp"(%2) : (!torch.vtensor<[3,4,5],f32>) -> !torch.vtensor<[3,4,5],f32>
    %4 = torch.operator "onnx.ReduceSum"(%3, %0) {torch.onnx.keepdims = 1 : si64} : (!torch.vtensor<[3,4,5],f32>, !torch.vtensor<[1],si64>) -> !torch.vtensor<[3,4,1],f32>
    %5 = torch.operator "onnx.Div"(%3, %4) : (!torch.vtensor<[3,4,5],f32>, !torch.vtensor<[3,4,1],f32>) -> !torch.vtensor<[3,4,5],f32>
    return %5 : !torch.vtensor<[3,4,5],f32>
  }
}
