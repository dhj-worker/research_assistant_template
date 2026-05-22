# TRELLIS: Structured 3D Latents for Scalable and Versatile 3D Generation

## 메타데이터

- PDF 파일: `TRELLIS_Structured 3D Latents for Scalable and Versatile 3D Generation.pdf`
- 논문 제목: TRELLIS: Structured 3D Latents for Scalable and Versatile 3D Generation
- 저자: Jianfeng Xiang, Zelong Lv, Sicheng Xu, Yu Deng, Ruicheng Wang, Bowen Zhang, Dong Chen, Xin Tong, Jiaolong Yang
- 소속: Tsinghua University, USTC, Microsoft Research
- venue/arXiv: arXiv:2412.01506v3 [cs.CV]
- 연도: 2025
- DOI/URL: https://github.com/Microsoft/TRELLIS
- 작업 일시: 2026-05-22

## Abstract

We introduce a novel 3D generation method for versatile and high-quality 3D asset creation.

**우리는 범용적이고 고품질인 3D asset 생성을 위한 새로운 3D generation 방법을 제안한다.**

The cornerstone is a unified Structured LATent (SLAT) representation which allows decoding to different output formats, such as Radiance Fields, 3D Gaussians, and meshes.

**핵심은 통합된 Structured LATent, 즉 SLAT 표현으로, 이를 통해 Radiance Fields, 3D Gaussians, mesh와 같은 서로 다른 출력 형식으로 decoding할 수 있다.**

This is achieved by integrating a sparsely-populated 3D grid with dense multiview visual features extracted from a powerful vision foundation model, comprehensively capturing both structural (geometry) and textural (appearance) information while maintaining flexibility during decoding.

**이는 sparse하게 채워진 3D grid와 강력한 vision foundation model에서 추출한 dense multiview visual feature를 결합함으로써 달성되며, decoding의 유연성을 유지하면서 structural 정보인 geometry와 textural 정보인 appearance를 포괄적으로 포착한다.**

We employ rectified flow transformers tailored for SLAT as our 3D generation models and train models with up to 2 billion parameters on a large 3D asset dataset of 500K diverse objects.

**우리는 SLAT에 맞게 설계된 rectified flow transformer를 3D generation model로 사용하고, 50만 개의 다양한 object로 구성된 대규모 3D asset dataset에서 최대 20억 parameter 규모의 model을 학습한다.**

Our model generates high-quality results with text or image conditions, significantly surpassing existing methods, including recent ones at similar scales.

**제안 모델은 text 또는 image condition에서 고품질 결과를 생성하며, 유사한 규모의 최신 방법을 포함한 기존 방법들을 크게 능가한다.**

We showcase flexible output format selection and local 3D editing capabilities which were not offered by previous models.

**또한 기존 모델이 제공하지 못했던 유연한 출력 형식 선택과 local 3D editing 능력을 보인다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 다시 확인했다.

1. Introduction
2. Related Works
   1. 3D generative models
   2. 3D creation with 2D generative models
   3. Rectified flow models
3. Methodology
   1. Structured Latent Representation
   2. Structured Latents Encoding and Decoding
   3. Structured Latents Generation
   4. 3D Editing with Structured Latents
4. Experiments
   1. Reconstruction Results
   2. Generation Results
   3. Ablation Study
   4. Applications
5. Conclusion
6. Supplementary Material
   1. More Implementation Details
   2. Data Preparation Details
   3. Evaluation Details
   4. More Results
   5. Limitations and Future works

## 요약

### 1. 전체 구조

이 논문은 3D asset generation의 병목을 "어떤 3D representation을 latent space로 삼을 것인가"라는 문제로 본다. Mesh/implicit field 계열은 geometry에는 강하지만 appearance modeling이 약하고, Radiance Field/3D Gaussian 계열은 rendering fidelity가 좋지만 표면 geometry 추출과 downstream 활용성이 약하다. TRELLIS는 이 representation별 trade-off를 피하기 위해 sparse 3D grid 위의 local latent 집합인 SLAT를 정의하고, 하나의 latent에서 3D Gaussian, Radiance Field, mesh를 모두 decoding한다.

핵심 pipeline은 세 단계로 볼 수 있다.

1. 3D asset을 active voxel과 local latent로 이루어진 SLAT로 encode한다.
2. Text/image condition에서 먼저 sparse structure를 생성하고, 그 위에 local latent를 생성한다.
3. 필요에 따라 Gaussian, Radiance Field, mesh decoder를 선택해 최종 3D representation으로 변환한다.

TRELLIS의 중요한 설계 철학은 "native 3D generation"과 "foundation visual feature"를 결합하는 것이다. 2D diffusion을 직접 distillation하거나 multi-view image reconstruction에 의존하는 대신, 3D asset dataset에서 SLAT 자체의 distribution을 학습한다. 동시에 DINOv2에서 추출한 dense multiview feature를 voxel에 aggregate해서 appearance와 geometry detail을 local latent에 넣는다.

### 2. Section 간 연결

Introduction은 3D generation에서 representation이 파편화되어 있다는 문제를 제기한다. Related Works는 기존 3D generative model, 2D-assisted 3D creation, rectified flow를 분리해 배경을 정리한다. Methodology는 SLAT의 정의, SLAT VAE, multi-format decoder, two-stage rectified flow generation, editing 방법을 순서대로 제시한다. Experiments는 같은 latent가 reconstruction fidelity와 generation quality 양쪽에서 효과적인지 검증하고, ablation으로 latent resolution, rectified flow, model scaling의 기여를 분리한다. Supplementary는 network architecture, training loss, data curation, evaluation protocol, limitations를 보강한다.

논문의 흐름은 비교적 일관적이다. 먼저 "표현을 통일해야 한다"는 주장을 세우고, SLAT가 reconstruction에서 다양한 output format을 보존한다는 것을 보인 뒤, 이 latent를 생성하는 TRELLIS가 text/image-to-3D에서 기존 방법보다 낫다는 실험으로 이어진다. 즉 reconstruction 결과는 SLAT 자체의 표현력을 검증하고, generation 결과는 SLAT 위의 generative modeling이 scalable하다는 점을 검증한다.

### 3. 핵심 주장과 근거

첫째, SLAT는 geometry와 appearance를 동시에 담는 versatile 3D latent이다. 논문은 active voxel이 coarse structure를 담당하고, 각 voxel의 latent가 local appearance/shape detail을 담당한다고 본다. 기본 grid resolution은 $N=64$이며, 평균 active voxel 수는 약 $L=20K$라고 보고한다. Sparse 구조 덕분에 전체 $N^3$ voxel을 모두 다루지 않고도 고해상도 3D 구조를 다룰 수 있다.

SLAT의 정의는 다음과 같다.

$$
z = \{(z_i, p_i)\}_{i=1}^{L}, \quad z_i \in \mathbb{R}^{C}, \quad p_i \in \{0, 1, \ldots, N-1\}^{3}
$$

여기서 $p_i$는 surface와 교차하는 active voxel의 position index이고, $z_i$는 해당 voxel에 붙은 local latent이다.

둘째, dense multiview DINOv2 feature를 voxel에 aggregate하는 방식이 fitting-free 3D encoding을 가능하게 한다. 각 3D asset을 여러 camera view에서 render하고, DINOv2 feature map을 얻은 뒤 active voxel을 각 view에 project하여 대응 feature를 평균한다. 이 feature를 sparse transformer VAE가 SLAT로 압축하고, decoder가 3D Gaussian, Radiance Field, mesh로 복원한다. 3DTopia-XL처럼 primitive fitting을 요구하거나 representation-specific fitting을 수행하는 접근보다 training object preparation 비용을 줄이는 방향이다.

셋째, generation은 two-stage rectified flow가 담당한다. 첫 번째 모델 $G_S$는 active voxel structure를 생성하고, 두 번째 모델 $G_L$은 주어진 structure 위의 local latent를 생성한다. Rectified flow는 data sample $x_0$와 noise 사이를 선형 보간한다.

$$
x(t) = (1 - t)x_0 + t\epsilon
$$

그리고 conditional flow matching objective는 다음 형태로 학습된다.

$$
L_{\mathrm{CFM}}(\theta)
= \mathbb{E}_{t, x_0, \epsilon}
\left\lVert v_\theta(x, t) - (\epsilon - x_0) \right\rVert_2^2
$$

논문은 diffusion baseline보다 rectified flow가 stage 1과 stage 2 모두에서 CLIP score와 FD를 개선한다고 보고한다.

넷째, locality가 editing을 쉽게 만든다. SLAT는 coarse structure와 local latent를 분리하므로, structure를 고정하고 latent만 다시 sample하면 shape outline은 유지하면서 detail variation을 만들 수 있다. Region-specific editing은 target bounding box 안의 voxel/latent만 RePaint 방식으로 resampling하고 나머지는 고정하는 방식이다.

### 4. Robotics 관점의 novelty와 relevance

Robotics 관점에서 TRELLIS의 강점은 "생성 asset을 여러 representation으로 꺼낼 수 있다"는 점이다. 3D Gaussian이나 Radiance Field는 photorealistic rendering, perception simulation, synthetic data generation에 유리하고, mesh는 collision checking, manipulation planning, physics simulation, digital twin asset pipeline에 더 적합하다. 하나의 latent에서 appearance-rich representation과 geometry-oriented representation을 모두 decoding할 수 있다는 점은 robot learning 환경 구축에 매력적이다.

또한 3D-FUTURE, HSSD, ABO처럼 indoor/furniture/object 중심 dataset을 포함하고 있어 household robotics나 embodied AI scene asset generation과 연결성이 있다. Supplementary의 scene composition 결과도 generated asset을 조합해 복합 scene을 만들 수 있음을 보여준다.

다만 robotics deployment에서는 주의가 필요하다. 논문은 visual/geometry metric과 user preference를 중심으로 평가하며, metric scale, watertightness, physical stability, material/PBR correctness, articulation, grasp affordance, collision validity는 직접 검증하지 않는다. Mesh decoder가 FlexiCubes 기반으로 geometry를 생성하지만, 실제 robot simulation에서 요구되는 manifoldness, inertia, contact behavior, texture-light disentanglement까지 보장한다고 보기는 어렵다. 따라서 TRELLIS는 robot-ready asset generator라기보다, robotics용 synthetic asset 후보를 빠르게 생성하는 foundation model에 가깝다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | 본 논문 | 의미 |
|---|---|---|---|
| Representation | Mesh/SDF, point cloud, triplane, Gaussian 등 representation별 latent가 분리됨 | Sparse voxel position과 local latent로 구성된 SLAT를 사용 | 하나의 latent에서 3D Gaussian, Radiance Field, mesh decoding 가능 |
| 2D-assisted 3D generation | 2D diffusion 기반 multi-view generation 후 reconstruction 또는 distillation | 3D asset dataset에서 native 3D latent distribution 학습 | Multi-view inconsistency로 인한 geometry distortion을 줄이는 방향 |
| Latent construction | Primitive fitting, representation-specific encoder, raw 3D fitting이 필요한 경우가 많음 | DINOv2 multiview feature를 active voxel에 aggregate하고 sparse VAE로 encoding | Fitting-free training과 detail-rich local feature를 동시에 추구 |
| Generation model | Diffusion 또는 autoregressive model 중심 | Two-stage rectified flow transformer | 논문 ablation에서 diffusion보다 prompt alignment와 quality가 좋음 |
| Output flexibility | 특정 output format에 묶이는 경우가 많음 | Decoder 선택으로 Gaussian/RF/mesh를 출력 | Rendering과 geometry downstream을 동시에 겨냥 |
| Editing | 대부분 별도 optimization 또는 fine-tuning 필요 | SLAT locality와 RePaint-style sampling으로 tuning-free local editing | Region deletion/addition/replacement가 가능 |

정량적으로 reconstruction에서는 SLAT가 LN3Diff, 3DTopia-XL, CLAY보다 좋은 결과를 보인다. Table 1에서 Ours는 appearance PSNR $32.74/32.19$, LPIPS $0.025/0.029$, CD $0.0083$, F-score $0.9999$, PSNR-N $36.11$, LPIPS-N $0.024$를 보고한다. CLAY는 shape-only 성격이 강한 baseline인데도 geometry에서 TRELLIS가 CD와 F-score를 앞선다는 점을 강조한다.

Generation에서는 Toys4k 기준 text-to-3D와 image-to-3D 모두에서 CLIP, FD, KD, FDpoint가 개선된다. Text-to-3D에서 Ours XL은 CLIP $26.70$, FD-inception $20.48$, KD-inception $0.08$, FD-DINOv2 $237.48$, KD-DINOv2 $4.10$, FD-point $5.21$을 보고한다. Image-to-3D에서는 Ours L이 CLIP $85.77$, FD-inception $9.35$, KD-inception $0.02$, FD-DINOv2 $67.21$, KD-DINOv2 $0.72$, FD-point $2.03$으로 강한 결과를 보인다. User study에서도 text prompt는 $67.1\%$, image prompt는 $94.5\%$ 선호를 얻었다고 보고한다.

### 6. Implementation idea

구현 관점에서 TRELLIS는 다음과 같은 구성으로 볼 수 있다.

1. 3D asset preprocessing
   - Mesh/asset을 정규화하고, surface와 교차하는 active voxel을 $64^3$ grid에서 찾는다.
   - 각 asset에 대해 150개 view를 render한다.
   - DINOv2 feature map을 추출하고 active voxel별로 multiview feature를 평균 aggregate한다.

2. SLAT VAE 학습
   - Sparse transformer encoder $E$가 voxelized feature $f = \{(f_i, p_i)\}_{i=1}^{L}$를 SLAT $z$로 encode한다.
   - Decoder $D_{GS}$, $D_{RF}$, $D_M$가 각각 3D Gaussian, Radiance Field, mesh를 복원한다.
   - 논문은 encoder/decoder를 Gaussian reconstruction으로 end-to-end 학습한 뒤, encoder를 freeze하고 Radiance Field 및 mesh decoder를 별도 학습한다.

3. Structure generation
   - Active voxel set을 dense binary grid $O \in \{0, 1\}^{N \times N \times N}$로 변환한다.
   - 3D convolutional VAE가 이를 저해상도 continuous feature grid $S$로 압축한다.
   - Transformer $G_S$가 text CLIP feature 또는 image DINOv2 feature condition에서 $S$를 rectified flow로 생성한다.

4. Latent generation
   - 생성된 active voxel structure 위에 noisy local latent를 두고 sparse transformer $G_L$이 denoising한다.
   - Sparse convolutional downsampler/upsampler와 skip connection으로 $2^3$ local packing을 사용해 efficiency를 높인다.

5. Decoding
   - Fast preview나 photorealistic rendering이 필요하면 3D Gaussian 또는 Radiance Field decoder를 사용한다.
   - Geometry export나 simulation 후보가 필요하면 mesh decoder를 사용한다.

Decoder별 설계도 명확하다. Gaussian decoder는 각 active voxel마다 $K=32$개 Gaussian의 offset, color, scale, opacity, rotation을 예측한다. Radiance Field decoder는 local $8^3$ radiance volume을 CP decomposition 형태로 예측해 $512^3$ radiance field로 조립한다. Mesh decoder는 FlexiCubes parameter와 SDF를 예측하고 sparse convolutional upsampling으로 $256^3$ resolution의 mesh extraction을 수행한다.

### 7. Mathematical background

SLAT는 sparse set representation과 grid locality를 결합한 latent이다. Active voxel set은 surface occupancy의 coarse geometry를 제공하고, local latent는 해당 영역의 fine appearance/shape feature를 제공한다. 이 구성은 point set처럼 variable-length이면서도 voxel grid처럼 spatial indexing이 가능하다.

3D Gaussian decoder는 local latent $z_i$를 voxel 주변의 Gaussian primitive로 변환한다.

$$
D_{GS}: \{(z_i, p_i)\}_{i=1}^{L}
\rightarrow
\left\{\left\{(o_i^k, c_i^k, s_i^k, \alpha_i^k, r_i^k)\right\}_{k=1}^{K}\right\}_{i=1}^{L}
$$

Gaussian의 최종 위치는 voxel locality를 유지하기 위해 다음처럼 제한된다.

$$
x_i^k = p_i + \tanh(o_i^k)
$$

Radiance Field decoder는 local radiance volume을 CP decomposition으로 표현한다.

$$
D_{RF}: \{(z_i, p_i)\}_{i=1}^{L}
\rightarrow
\{(v_i^x, v_i^y, v_i^z, v_i^c)\}_{i=1}^{L}
$$

Mesh decoder는 FlexiCubes parameter와 SDF를 예측한다.

$$
D_M: \{(z_i, p_i)\}_{i=1}^{L}
\rightarrow
\left\{\{(w_i^j, d_i^j)\}_{j=1}^{64}\right\}_{i=1}^{L}
$$

Supplementary에서는 mesh decoder가 color와 normal도 함께 예측한다고 설명한다. Loss는 Gaussian/RF의 경우 rendering reconstruction loss가 중심이며, Gaussian은 volume/opacity regularization을 추가한다. Mesh는 mask, depth, normal, color, regularization을 결합한다.

$$
L_{\mathrm{recon}} = L_1 + 0.2(1 - \mathrm{SSIM}) + 0.2\mathrm{LPIPS}
$$

Mesh geometry loss는 foreground mask, depth, normal reconstruction을 포함한다.

$$
L_{\mathrm{geo}} = L_1(M) + 10L_{\mathrm{Huber}}(D) + L_{\mathrm{recon}}(N_m)
$$

이 수식들은 TRELLIS가 단순히 visual feature를 latent로 쓰는 것이 아니라, decoder별 differentiable rendering objective를 통해 output representation에 맞는 복원 성질을 부여한다는 점을 보여준다.

### 8. Experiments

학습 데이터는 Objaverse-XL, ABO, 3D-FUTURE, HSSD에서 curated된 약 500K개 3D asset이다. Supplementary Table 8 기준 filtered size는 ObjaverseXL Sketchfab $168{,}307$, ObjaverseXL GitHub $311{,}843$, ABO $4{,}485$, 3D-FUTURE $9{,}472$, HSSD $6{,}670$으로 총 약 $500{,}777$개다. Toys4k는 training set에 포함하지 않고 evaluation set으로 사용하며, aesthetic score threshold 적용 후 $3{,}229$개를 사용한다.

Training setup은 꽤 크다. Basic, Large, X-Large model은 각각 약 342M, 1.1B, 2B parameter 규모이고, XL은 64개의 A100 40GB GPU에서 batch size 256으로 400K step 학습된다. AdamW learning rate는 $1e-4$, classifier-free guidance drop rate는 $0.1$, inference CFG strength는 3, sampling step은 50이다.

Reconstruction evaluation은 Toys4k filtered subset 500개를 대상으로 appearance fidelity와 geometry accuracy를 본다. Appearance는 random camera render에서 PSNR/LPIPS를 계산한다. Geometry는 rendered depth를 unproject해 100K point를 sample하고 CD/F-score를 계산하며, normal map render에 대한 PSNR-N/LPIPS-N도 사용한다.

Generation evaluation은 Toys4k 1,250개 subset과 training set 5,000개 subset을 사용한다. Appearance quality는 rendered 4-view image에서 FD/KD를 Inception-v3와 DINOv2 feature로 계산하고, geometry quality는 PointNet++ 기반 FDpoint를 사용한다. Prompt consistency는 CLIP score로 평가한다.

Ablation의 결론은 세 가지다.

1. SLAT resolution은 $32^3$에서 channel을 늘리는 것보다 $64^3$로 올리는 것이 더 효과적이다. Table 3에서 $64^3$, channel 8 설정이 PSNR $32.74$, LPIPS $0.0250$으로 가장 좋다.
2. Diffusion보다 rectified flow가 stage 1과 stage 2 모두에서 좋다. Stage 1을 rectified flow로 바꾸면 Toys4k CLIP이 $25.86$에서 $26.37$로, FD-DINOv2가 $295.90$에서 $269.56$으로 개선된다. Stage 2에서도 Toys4k FD-DINOv2가 $244.08$에서 $240.20$으로 개선된다.
3. Model size scaling은 계속 유효하다. B, L, XL로 갈수록 training set과 Toys4k 모두에서 CLIP이 오르고 FD-DINOv2가 낮아진다.

실험의 강점은 reconstruction, generation, ablation, user study가 서로 다른 측면을 검증한다는 점이다. 약점은 commercial model과의 비교가 supplementary의 qualitative comparison 중심이고, 물리적/semantic correctness나 robotics-grade geometry validity 평가는 없다는 점이다.

### 9. Limitations and future work

논문이 명시한 limitation은 두 가지다.

1. Two-stage generation pipeline은 sparse structure를 먼저 생성하고 그 위의 local latent를 생성하므로, complete 3D asset을 single stage로 만드는 end-to-end 방법보다 비효율적일 수 있다.
2. Image-to-3D model은 lighting effect를 분리하지 못해 reference image의 shading과 highlight가 asset에 baked-in될 수 있다. 저자들은 더 robust한 lighting augmentation과 PBR material prediction을 future work로 제안한다.

추가로 읽을 때 주의할 점은 다음과 같다.

- Local editing은 bounding box 기반 region control에 가깝고, semantic part segmentation이나 articulation-aware editing은 아니다.
- Mesh output이 가능하지만 simulation-ready mesh라고 검증되지는 않았다.
- Text/image prompt는 GPT-4, DALL-E 3, GPT-4o captioning pipeline과 강하게 연결되어 있어, prompt distribution과 caption quality의 영향이 크다.
- Dataset curation은 aesthetic predictor 기반 filtering을 사용하므로, low-quality scan이나 robotics 현장의 noisy object distribution에 대한 robustness는 별도 검증이 필요하다.
- 2B model 학습 비용이 크기 때문에 재현성은 code/model/data release가 있더라도 hardware barrier가 있다.

### 10. 결론

TRELLIS는 3D generation에서 "좋은 latent representation"이 output format보다 더 근본적인 병목이라는 관점을 제시한다. SLAT는 sparse voxel structure와 DINOv2 기반 local visual feature를 결합해 geometry와 appearance를 함께 담고, decoder 선택으로 Gaussian, Radiance Field, mesh를 출력한다. Two-stage rectified flow transformer는 이 SLAT distribution을 text/image condition에서 직접 생성한다.

논문의 contribution은 단순히 더 큰 text-to-3D model을 만든 것이 아니라, representation-agnostic 3D asset generation을 위한 latent space 설계를 제안했다는 데 있다. Robotics에서는 photorealistic synthetic data, scene asset generation, simulation candidate mesh 생성에 유용할 수 있지만, 실제 manipulation/planning/simulation에 쓰려면 physical validity, scale, PBR material, collision geometry 검증이 뒤따라야 한다.

## 추가 질문과 답변
