# TRELLIS2: Native and Compact Structured Latents for 3D Generation

## 메타데이터

- PDF 파일: `TRELLIS2_Native and Compact Structured Latents for 3D Generation.pdf`
- 논문 제목: Native and Compact Structured Latents for 3D Generation
- 저자: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- 소속: Tsinghua University, Microsoft Research, USTC, Microsoft AI
- venue/arXiv: arXiv:2512.14692v1 [cs.CV]
- 연도: 2025
- DOI/URL: https://microsoft.github.io/TRELLIS.2
- 작업 일시: 2026-05-22

## Abstract

Recent advancements in 3D generative modeling have significantly improved the generation realism, yet the field is still hampered by existing representations, which struggle to capture assets with complex topologies and detailed appearance.

**최근 3D generative modeling의 발전은 생성 realism을 크게 개선했지만, 이 분야는 여전히 복잡한 topology와 세밀한 appearance를 가진 asset을 포착하기 어려운 기존 representation에 의해 제약을 받고 있다.**

This paper presents an approach for learning a structured latent representation from native 3D data to address this challenge.

**이 논문은 이러한 문제를 해결하기 위해 native 3D data로부터 structured latent representation을 학습하는 접근을 제시한다.**

At its core is a new sparse voxel structure called O-Voxel, an omni-voxel representation that encodes both geometry and appearance.

**핵심에는 O-Voxel이라는 새로운 sparse voxel structure가 있으며, 이는 geometry와 appearance를 모두 encode하는 omni-voxel representation이다.**

O-Voxel can robustly model arbitrary topology, including open, non-manifold, and fully-enclosed surfaces, while capturing comprehensive surface attributes beyond texture color, such as physically-based rendering parameters.

**O-Voxel은 open surface, non-manifold surface, fully-enclosed surface를 포함한 arbitrary topology를 robust하게 model할 수 있으며, texture color를 넘어 physically-based rendering parameter 같은 포괄적인 surface attribute를 포착한다.**

Based on O-Voxel, we design a Sparse Compression VAE which provides a high spatial compression rate and a compact latent space.

**O-Voxel을 기반으로, 저자들은 높은 spatial compression rate와 compact latent space를 제공하는 Sparse Compression VAE를 설계한다.**

We train large-scale flow-matching models comprising 4B parameters for 3D generation using diverse public 3D asset datasets.

**저자들은 다양한 공개 3D asset dataset을 사용해 총 40억 parameter 규모의 large-scale flow-matching model을 3D generation용으로 학습한다.**

Despite their scale, inference remains highly efficient.

**이러한 규모에도 불구하고 inference는 매우 효율적으로 유지된다.**

Meanwhile, the geometry and material quality of our generated assets far exceed those of existing models.

**동시에 생성된 asset의 geometry와 material quality는 기존 model들을 크게 능가한다.**

We believe our approach offers a significant advancement in 3D generative modeling.

**저자들은 이 접근이 3D generative modeling에서 중요한 진전을 제공한다고 본다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다.

1. Introduction
2. Related Work
   1. 3D Representations for Generation
   2. Latent 3D Representations
   3. Large 3D Asset Generation Models and Systems
3. Method
   1. O-Voxel: A Native 3D Representation
      1. Flexible Dual Grid for Shape
      2. Volumetric Attributes for Material
   2. Sparse Compression VAE
      1. Network Architecture
      2. VAE Training
   3. Generative Modeling
4. Experiments
   1. 3D Asset Reconstruction
   2. Image to 3D Generation
   3. Shape-Conditioned Texture Generation
   4. Ablation and Design Analysis
   5. Test-time Compute and Resolution Scaling
5. Conclusion
6. Supplementary Material
   1. O-Voxel Conversion Algorithms
   2. Network Architectures
   3. Training Details
   4. FlexGEMM: Our High-Performance Sparse Convolution Backend
   5. Data Preparation Details
   6. More Experiment Details
   7. More Results
   8. Limitation Discussion and Future Work

## 요약

### 1. 전체 구조

TRELLIS2는 TRELLIS 계열의 핵심 질문을 한 단계 더 밀어붙인다. TRELLIS가 sparse voxel structure와 DINOv2 multiview feature를 결합한 SLAT로 versatile 3D asset generation을 수행했다면, TRELLIS2는 이 latent를 native 3D data에서 직접 학습하고 더 compact하게 압축하는 것을 목표로 한다. 논문이 문제 삼는 지점은 기존 representation들이 open surface, non-manifold geometry, enclosed interior, PBR material을 동시에 잘 다루지 못한다는 점이다.

전체 pipeline은 다음 세 단계로 볼 수 있다.

1. Mesh asset을 O-Voxel이라는 field-free sparse voxel representation으로 즉시 변환한다.
2. O-Voxel을 Sparse Compression VAE, 즉 SC-VAE로 압축해 compact structured latent space를 만든다.
3. Flow-matching DiT model 세 개가 sparse structure, geometry latent, material latent를 순차적으로 생성한다.

논문의 가장 중요한 방향 전환은 “2D feature에서 3D latent를 구성한다”가 아니라 “mesh와 PBR material에서 바로 native 3D representation을 만들고, 그 representation을 compact latent로 압축한다”는 점이다. 그래서 TRELLIS2는 geometry뿐 아니라 base color, metallic, roughness, opacity 같은 PBR attribute를 3D latent domain 안에서 직접 다룬다.

### 2. Section 간 연결

Introduction은 3D generation realism은 크게 좋아졌지만, representation bottleneck이 여전히 남아 있다고 진단한다. Iso-surface field 기반 표현은 watertight 또는 manifold 가정에 약하고, appearance/material 정보까지 함께 담기 어렵다. TRELLIS의 SLAT도 geometry와 appearance를 함께 다루지만, multiview 2D feature input과 rendering supervision에 의존해서 복잡한 structure와 material을 충분히 capture하지 못한다고 본다.

Related Work는 representation 문제를 세 갈래로 정리한다. 첫째, implicit field, SDF, NeRF, mesh, point cloud, Gaussian 같은 3D representation의 장단점이다. 둘째, unstructured latent와 sparse structured latent의 compression/fidelity trade-off다. 셋째, large 3D asset generation system들이 multi-view texture synthesis와 post-processing에 기대는 문제다.

Method는 이 bottleneck을 O-Voxel, SC-VAE, flow-matching generation으로 푼다. O-Voxel은 mesh와 neural network 사이의 native sparse representation이고, SC-VAE는 O-Voxel을 높은 spatial downsampling ratio로 압축한다. Generative Modeling section은 TRELLIS의 two-stage geometry generation을 확장해 material generation stage를 추가한다.

Experiments는 representation fidelity, image-to-3D generation quality, texture generation, ablation, test-time scaling을 차례로 확인한다. Supplementary는 O-Voxel 변환 algorithm, architecture, loss, dataset filtering, evaluation protocol, limitation을 보강한다.

### 3. 핵심 주장과 근거

첫째, O-Voxel은 field-free 3D asset representation이다. SDF처럼 sign change를 찾거나 flood-fill을 수행하지 않고, mesh surface가 voxel edge와 교차하는지를 직접 계산해 active voxel과 Hermite data를 만든다. O-Voxel은 다음 feature tuple 집합으로 정의된다.

$$
f = \{(f_i^{\mathrm{shape}}, f_i^{\mathrm{mat}}, p_i)\}_{i=1}^{L}
$$

여기서 $f_i^{\mathrm{shape}}$는 local geometry, $f_i^{\mathrm{mat}}$는 material property, $p_i \in \{0, 1, \ldots, N - 1\}^3$는 $N \times N \times N$ regular grid에서 $i$번째 active voxel의 좌표다. Empty voxel은 inactive로 둔다.

둘째, shape는 Flexible Dual Grid로 표현된다. 각 primal cell에 dual vertex 하나를 두고, primal edge 하나에 대응하는 quadrilateral face가 adjacent dual vertex를 연결한다. 논문은 Dual Contouring에서 온 QEF를 field 없이 mesh intersection data에 직접 적용한다. Hermite data $\{q_i, n_i\}$가 있을 때 dual vertex $v$는 다음 objective로 계산된다.

$$
\min_{v \in \mathrm{voxel}} e(v)
= \sum_i d_{\perp,i}^{2}
+ \lambda_{\mathrm{bound}}\sum_j d_{L,j}^{2}
+ \lambda_{\mathrm{reg}} d_{\bar{q}}^{2}
$$

원래 DC의 plane distance term에 더해, open surface boundary edge에 align하도록 boundary distance term을 추가하고, singularity를 줄이기 위해 intersection point 평균 $\bar{q}$ 근처에 머무르게 하는 regularization을 넣는다. 이 설계 때문에 open surface, self-intersection, fully-enclosed interior를 SDF preprocessing 없이 다룰 수 있다는 것이 저자들의 주장이다.

셋째, material은 surface geometry와 align된 volumetric attribute로 둔다. 각 active voxel의 material feature는 다음처럼 PBR parameter를 담는다.

$$
f_i^{\mathrm{mat}} = (c_i, m_i, r_i, \alpha_i)
$$

여기서 $c_i \in \mathbb{R}_{[0,1]}^3$는 base color, $m_i \in \mathbb{R}_{[0,1]}$는 metallic, $r_i \in \mathbb{R}_{[0,1]}$는 roughness, $\alpha_i \in \mathbb{R}_{[0,1]}$는 opacity다. Texture to O-Voxel 변환은 voxel center를 intersected triangle에 project하고 UV texture map에서 attribute를 sample한 뒤 distance-weighted average를 취한다. O-Voxel to texture 변환은 mesh vertex 또는 texel surface point에서 neighboring voxel attribute를 trilinear interpolation한다.

넷째, SC-VAE는 O-Voxel을 compact latent로 압축한다. Transformer 기반 sparse latent encoder 대신 fully sparse-convolutional U-shaped VAE를 사용한다. 핵심은 sparse residual autoencoding이다. Downsampling 때 8개 child voxel feature를 channel dimension으로 stack하고 group average로 coarse residual estimate를 만들며, upsampling 때는 channel-to-space shortcut으로 coarse feature를 child neighborhood에 distribute한다. Early-pruning upsampler는 inactive child voxel을 미리 건너뛰고, optimized residual block은 sparse convolution을 줄이고 point-wise MLP를 넣어 detail fidelity를 유지한다.

다섯째, generation은 세 stage로 분리된다.

1. Sparse structure generation: sparse voxel grid의 occupancy layout을 생성한다.
2. Geometry generation: active voxel 안의 geometry latent를 생성한다.
3. Material generation: input image와 generated geometry latent에 condition된 material latent를 생성한다.

각 DiT는 약 1.3B parameter이고, 세 모델 합산 약 4B parameter 규모다. Image condition feature는 DINOv3-L에서 추출한다. TRELLIS2는 SC-VAE의 높은 compression 덕분에 TRELLIS의 convolutional packing과 skip connection을 버리고 vanilla-style sparse DiT로 단순화했다고 설명한다.

### 4. Robotics 관점의 novelty와 relevance

Robotics 관점에서 가장 흥미로운 점은 TRELLIS2가 visual-only 3D asset이 아니라 PBR material과 arbitrary-topology geometry를 함께 생성하려 한다는 점이다. Base color만 있는 mesh보다 metallic, roughness, opacity가 있는 asset은 relighting, synthetic perception data, domain randomization, embodied AI simulation에서 훨씬 유용하다. 특히 opacity를 포함해 translucent surface를 다루려는 점은 glass, plastic, transparent container 같은 household robotics object를 고려할 때 의미가 있다.

또한 O-Voxel은 mesh와 즉시 양방향 변환을 목표로 한다. 이는 NeRF나 Gaussian-only asset보다 collision geometry, surface normal, mesh export, simulation candidate generation으로 이어지기 쉽다. Direct mesh reconstruction과 material reconstruction이 같은 3D coordinate structure에 align되므로, synthetic dataset을 만들 때 geometry와 appearance의 misalignment가 줄어들 가능성이 있다.

다만 robot-ready asset generator라고 보기는 아직 이르다. 논문은 geometry reconstruction, normal map fidelity, PBR render quality, user preference를 중심으로 평가한다. 물리 simulation에서 중요한 watertightness, manifoldness, collision stability, mass/inertia, scale calibration, articulation, affordance, graspability, material의 실제 friction/contact parameter는 평가하지 않는다. O-Voxel이 open/non-manifold를 잘 표현하는 능력은 reconstruction fidelity에는 좋지만, physics engine에 바로 넣기에는 후처리와 validation이 더 필요할 수 있다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | TRELLIS2 | 의미 |
|---|---|---|---|
| 3D representation | SDF, FlexiCubes, NeRF, Gaussian, mesh 등 representation별 장단점이 강함 | O-Voxel로 geometry와 PBR material을 sparse voxel tuple에 함께 encode | Open/non-manifold/enclosed structure와 material을 같은 native 3D structure에서 처리 |
| TRELLIS 대비 latent source | Multiview 2D visual feature 기반 SLAT | Mesh/PBR asset에서 직접 만든 native O-Voxel latent | 2D feature projection과 rendering-only supervision 의존을 줄임 |
| Topology | Field-based method는 watertight/manifold assumption에 취약 | Flexible Dual Grid가 open, non-manifold, fully-enclosed surface를 직접 다룸 | 복잡한 CAD-like 또는 scanned asset에 더 적합한 방향 |
| Material | Texture color 중심이거나 multi-view texture baking 필요 | Base color, metallic, roughness, opacity를 volumetric surface attribute로 encode | Relighting 가능한 PBR asset generation을 목표로 함 |
| Compression | Structured sparse latent는 fidelity는 좋지만 token 수가 많음 | SC-VAE가 $16\times$ spatial compression으로 1024급 asset을 약 9.6K token에 encode | Large DiT generation과 high-resolution scaling의 비용을 낮춤 |
| Generation | Shape generation 후 texture synthesis/post-processing을 붙이는 경우가 많음 | Sparse structure, geometry latent, material latent를 native 3D latent domain에서 순차 생성 | Shape-material alignment와 internal surface texture synthesis에 유리 |

정량 결과에서 TRELLIS2의 reconstruction fidelity는 강하게 나온다. Table 1에서 Ours 1024는 Toys4K 기준 9.6K token과 $16\times$ downsampling으로 MD $0.0042$, F1 $0.971$, CD $0.5660$, outer F1 $0.855$, normal PSNR $43.11$, LPIPS $0.005$를 보고한다. 같은 token 수의 TRELLIS는 MD $85.07$, CD $8.171$, normal PSNR $30.29$, LPIPS $0.067$이어서, 저자들이 말하는 native O-Voxel latent의 fidelity 이득이 매우 크게 나타난다.

Image-to-3D generation에서는 Table 2 기준 Ours가 CLIP $0.894$, CLIP-N $0.758$, ULIP-2 $0.477$, Uni3D $0.436$을 기록한다. User study에서는 overall quality $66.5\%$, shape quality $69.0\%$로 TRELLIS, Hunyuan3D 2.1, Step1X-3D, Direct3D-S2, Hi3DGen보다 선호율이 높다. Baseline 중 Hunyuan3D 2.1은 PBR material을 생성하지만, TRELLIS2는 더 sharp한 geometry와 prompt-aligned material을 보인다고 주장한다.

### 6. Implementation idea

구현 흐름을 asset processing pipeline으로 풀면 다음과 같다.

1. Mesh to O-Voxel
   - Mesh surface와 voxel edge의 intersection을 찾는다.
   - Intersected edge 주변 voxel을 active로 표시한다.
   - Intersection point와 normal로 Hermite data를 만든다.
   - QEF를 풀어 voxel별 dual vertex를 계산한다.
   - Edge intersection flag와 splitting weight로 quad/triangle connectivity를 구성한다.

2. Texture/PBR to O-Voxel
   - Active voxel center를 intersected triangle에 project한다.
   - UV map에서 base color, metallic, roughness, opacity를 sample한다.
   - Surface distance 기반 weighted average로 voxel material attribute를 정한다.

3. SC-VAE training
   - Shape SC-VAE와 material SC-VAE를 decoupled latent space로 학습한다.
   - Stage 1은 low-resolution O-Voxel direct reconstruction과 KL loss로 안정화한다.
   - Stage 2는 mask, depth, normal, material rendering loss를 추가해 high-resolution detail을 보강한다.
   - Material VAE는 shape VAE의 subdivision structure에 condition된다.

4. Generative model training
   - Structure DiT는 sparse occupancy layout을 만든다.
   - Geometry DiT는 active voxel별 geometry latent를 만든다.
   - Material DiT는 input image와 geometry latent에 condition되어 PBR material latent를 만든다.
   - Training은 512급에서 시작해 1024급으로 progressive하게 scale한다.

5. Inference
   - $512^3$ asset은 약 3초, $1024^3$ asset은 약 17초, $1536^3$ asset은 약 60초가 걸린다고 보고한다. 본문 Figure 1의 breakdown은 $1536^3$ generation에서 shape 약 35초, texture 약 25초를 보인다.
   - Test-time scaling에서는 generated O-Voxel을 downsample해 더 높은 sparse structure resolution을 만들고 geometry stage를 다시 적용하는 cascaded inference를 사용한다.

### 7. Mathematical background

O-Voxel의 장점은 set-like sparsity와 grid-like locality를 동시에 가진다는 데 있다. Active voxel만 유지하므로 dense $N^3$ volume보다 효율적이고, voxel coordinate $p_i$가 있으므로 sparse convolution과 DiT가 spatial structure를 활용할 수 있다.

Shape feature는 dual vertex $v_i$, edge intersection flag $\gamma_i$, splitting weight $\omega_i$로 구성된다. Material feature는 PBR tuple이다.

$$
f_i^{\mathrm{shape}} = (v_i, \gamma_i, \omega_i)
$$

$$
f_i^{\mathrm{mat}} = (c_i, m_i, r_i, \alpha_i)
$$

SC-VAE의 stage 1 loss는 O-Voxel feature reconstruction과 KL regularization으로 구성된다.

$$
L_{s1}
= \lambda_v \lVert \hat{v} - v \rVert_2^2
+ \lambda_{\gamma}\mathrm{BCE}(\hat{\gamma}, \gamma)
+ \lambda_{\pi}\mathrm{BCE}(\hat{\pi}, \pi)
+ \lambda_{\mathrm{mat}}\lVert \hat{f}^{\mathrm{mat}} - f^{\mathrm{mat}} \rVert_1
+ \lambda_{\mathrm{KL}}L_{\mathrm{KL}}
$$

여기서 $\pi$는 early-pruning mask로 읽을 수 있다. Stage 2는 rendering-based perceptual supervision을 추가한다.

$$
L_{s2} = L_{s1} + L_{\mathrm{render}}
$$

Supplementary는 rendering loss를 mask, depth, normal, material rendering term으로 더 구체화한다.

$$
d_p(a,b) = \lVert a - b \rVert_1 + 0.2 d_{\mathrm{SSIM}} + 0.2 d_{\mathrm{LPIPS}}
$$

$$
L_{\mathrm{render}}^{\mathrm{shape}}
= \lVert \hat{m} - m \rVert_1
+ 10\lVert \hat{d} - d \rVert_1
+ d_p(\hat{n}, n)
$$

$$
L_{\mathrm{render}}^{\mathrm{mat}}
= d_p(\hat{c}, c) + d_p(\widehat{mra}, mra)
$$

Generation model은 rectified flow/flow matching으로 학습된다. Forward path는 data sample $x_0$와 noise $\epsilon$ 사이의 linear interpolation이다.

$$
x(t) = (1 - t)x_0 + t\epsilon
$$

Conditional Flow Matching objective는 다음 형태다.

$$
L_{\mathrm{CFM}}(\theta)
= \mathbb{E}_{t, x_0, \epsilon}
\left[
\left\lVert v_{\theta}(x(t), t) - (\epsilon - x_0) \right\rVert_2^2
\right]
$$

논문은 logitNorm timestep sampling을 사용해 generation quality를 개선한다고 설명한다.

### 8. Experiments

SC-VAE 학습은 Trellis-500K setup을 기반으로 하되 PBR material이 없는 asset을 제거한다. Dataset은 Objaverse-XL, ABO, HSSD 중심이며, Supplementary Table 6에 따르면 SC-VAE training set은 shape available $473{,}349$개, material available $354{,}966$개다. Generative model training에는 TexVerse를 추가해 총 약 $800K$ asset으로 확장하고, Table 6 기준 all training set은 shape available $976{,}736$개, material available $737{,}962$개다. Evaluation에는 Toys4K $3{,}229$개 중 PBR 조건을 만족하는 subset과 Sketchfab Featured 90개 asset을 사용한다.

Reconstruction evaluation은 세 축이다. Mesh Distance와 MD F-score는 enclosed/internal surface까지 포함한 mesh fidelity를 본다. Chamfer Distance와 CD F-score는 rendered depth에서 unproject한 outer surface point cloud를 본다. Normal PSNR/LPIPS는 fine surface detail을 본다. Material reconstruction은 PBR attribute map과 shaded image의 PSNR/LPIPS로 측정하며, 본문은 PBR attribute $38.89$ dB / $0.033$, shaded image $38.69$ dB / $0.026$을 보고한다.

Image-to-3D generation은 AI-generated image prompt 100개를 사용한다. CLIP은 visual semantic alignment, ULIP-2와 Uni3D는 generated colored point cloud와 image prompt 사이의 3D-aware similarity를 측정한다. User study는 약 40명이 interactive turntable video를 보고 overall quality와 shape quality를 선택하는 방식으로 진행된다.

Shape-conditioned texture generation에서는 material stage를 독립적으로 사용해 mesh와 reference image가 주어졌을 때 PBR texture를 합성한다. Baseline은 Hunyuan3D-Paint와 TEXGen이다. 논문은 multi-view 방식이 view inconsistency, ghosting, blurred texture에 취약하고 UV 기반 방식은 seam artifact가 생긴다고 보며, native 3D material generation이 internal surface texture와 shape-material alignment에 유리하다고 주장한다.

Ablation은 SC-VAE 설계의 기여를 분리한다. Sparse residual autoencoding을 제거하면 $16\times$ compression에서 MD가 $69\%$ 증가하고 PSNR이 $0.5$ dB 감소하며, $32\times$ compression에서는 MD 증가가 $526\%$, PSNR 감소가 $1.6$ dB까지 악화된다. Optimized residual block을 표준 residual block으로 바꾸면 MD가 $16\%$ 증가하고 PSNR이 $0.6$ dB 감소한다. 즉 compact latent의 성능은 단순 sparse convolution이 아니라 residual autoencoding과 block 설계에 크게 의존한다.

### 9. Limitations and future work

논문이 명시한 limitation은 세 가지다.

1. O-Voxel의 representation power는 spatial resolution에 의해 제한된다. Voxel보다 작은 두 parallel surface가 같은 voxel 안에 들어오면 QEF solution이 두 surface 사이에 놓일 수 있고, material attribute도 평균화되어 blurred appearance가 생길 수 있다.
2. Reconstruction과 generation 결과에 작은 hole이 생길 수 있다. 저자들은 standard mesh post-processing, 예를 들어 hole filling으로 대부분 고칠 수 있다고 하지만, sparse decoder가 완전히 closed manifold surface를 안정적으로 보장하는 것은 아직 어렵다고 본다.
3. O-Voxel은 현재 geometry와 material에 초점을 맞추며, higher-level structural 또는 semantic information을 명시적으로 encode하지 않는다. 저자들은 part-level segmentation과 graph-based topological structure를 future work로 제안한다.

Robotics 관점의 추가 한계도 있다. 논문은 material을 PBR parameter로 다루지만, 실제 contact property나 dynamics parameter까지 예측하지 않는다. 투명/반사 object의 visual material은 다루지만, robot perception에서 중요한 multi-sensor behavior, depth sensor failure, scale ambiguity, occlusion robustness는 평가하지 않는다. 또한 generation은 image-conditioned open-domain asset 생성 중심이라, robot task에 필요한 affordance-preserving generation이나 articulated object modeling은 아직 별도 문제로 남는다.

### 10. 결론

TRELLIS2의 contribution은 “더 큰 3D generator”보다는 “native 3D asset을 compact structured latent로 만드는 representation 설계”에 있다. O-Voxel은 Flexible Dual Grid로 arbitrary topology geometry를 표현하고, volumetric PBR attribute로 material을 surface와 align한다. SC-VAE는 이를 $16\times$ spatial compression으로 압축해 large flow-matching DiT가 다룰 수 있는 latent space를 만든다.

TRELLIS 대비 핵심 개선은 multiview 2D feature 기반 SLAT에서 native O-Voxel 기반 latent로 옮겨갔다는 점, 그리고 geometry와 material generation을 같은 3D latent domain에서 직접 수행한다는 점이다. 실험 결과는 reconstruction fidelity, image-to-3D generation, user study, PBR texture synthesis에서 강하다. 다만 simulation-ready asset, robotics manipulation asset, physically valid material까지 보장하려면 mesh validation, scale/physics annotation, articulation/affordance modeling이 추가로 필요하다.

## 추가 질문과 답변
