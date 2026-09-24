import  numpy as np

mamoth_feature = np.ones((1000,1000), dtype =np.float64)
scale_factor = 2.5
output_buffer = np.empty_like(mamoth_feature)
# print("Before scaling:\n", mamoth_feature)
# print("output_buffer before scaling:\n", output_buffer)
np.multiply(mamoth_feature, scale_factor, out=output_buffer)
# print("After scaling:\n", output_buffer)
# print("mamoth_feature remains unchanged:\n", mamoth_feature)

# print("shape output_buffer:\n", output_buffer.shape)
# print("sample output_buffer:\n", output_buffer[:5,:5])
print("Memory buffer identity check:\n",np.may_share_memory(mamoth_feature, output_buffer))
print("_" * 60)