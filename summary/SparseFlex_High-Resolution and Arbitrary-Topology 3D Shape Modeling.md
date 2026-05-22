# SparseFlex: High-Resolution and Arbitrary-Topology 3D Shape Modeling

## 메타데이터

- PDF 파일: `SparseFlex_High-Resolution and Arbitrary-Topology 3D Shape Modeling.pdf`
- 논문 제목: SparseFlex: High-Resolution and Arbitrary-Topology 3D Shape Modeling
- 저자: Xianglong He, Zi-Xin Zou, Chia-Hao Chen, Yuan-Chen Guo, Ding Liang, Chun Yuan, Wanli Ouyang, Yan-Pei Cao, Yangguang Li
- 소속: Tsinghua University, VAST, The Chinese University of Hong Kong
- venue/arXiv: arXiv:2503.21732v1 [cs.CV]
- 연도: 2025
- DOI/URL: https://arxiv.org/abs/2503.21732, https://xianglonghe.github.io/TripoSF
- 작업 일시: 2026-05-22

## Abstract

Creating high-fidelity 3D meshes with arbitrary topology, including open surfaces and complex interiors, remains a significant challenge.

**open surface와 복잡한 내부 구조를 포함해 arbitrary topology를 갖는 고충실도 3D mesh를 만드는 것은 여전히 중요한 난제이다.**

Existing implicit field methods often require costly and detail-degrading watertight conversion, while other approaches struggle with high resolutions.

**기존 implicit field 방법들은 비용이 크고 세부 형상을 손상시키는 watertight conversion을 요구하는 경우가 많으며, 다른 접근들은 고해상도에서 어려움을 겪는다.**

This paper introduces SparseFlex, a novel sparse-structured isosurface representation that enables differentiable mesh reconstruction at resolutions up to $1024^3$ directly from rendering losses.

**이 논문은 rendering loss로부터 직접 최대 $1024^3$ 해상도의 differentiable mesh reconstruction을 가능하게 하는 새로운 sparse-structured isosurface representation인 SparseFlex를 제안한다.**

SparseFlex combines the accuracy of Flexicubes with a sparse voxel structure, focusing computation on surface-adjacent regions and efficiently handling open surfaces.

**SparseFlex는 FlexiCubes의 정확성과 sparse voxel structure를 결합하여 계산을 surface-adjacent region에 집중시키고 open surface를 효율적으로 처리한다.**

Crucially, we introduce a frustum-aware sectional voxel training strategy that activates only relevant voxels during rendering, dramatically reducing memory consumption and enabling high-resolution training.

**핵심적으로 저자들은 rendering 중 관련 voxel만 활성화하는 frustum-aware sectional voxel training 전략을 도입하여 memory consumption을 크게 줄이고 고해상도 학습을 가능하게 한다.**

This also allows, for the first time, the reconstruction of mesh interiors using only rendering supervision.

**이 전략은 또한 rendering supervision만으로 mesh interior를 재구성하는 것을 처음으로 가능하게 한다고 주장한다.**

Building upon this, we demonstrate a complete shape modeling pipeline by training a variational autoencoder (VAE) and a rectified flow transformer for high-quality 3D shape generation.

**이를 바탕으로 저자들은 고품질 3D shape generation을 위해 VAE와 rectified flow transformer를 학습하는 완전한 shape modeling pipeline을 보인다.**

Our experiments show state-of-the-art reconstruction accuracy, with a 82% reduction in Chamfer Distance and a 88% increase in F-score compared to previous methods, and demonstrate the generation of high-resolution, detailed 3D shapes with arbitrary topology.

**실험은 이전 방법 대비 Chamfer Distance 82% 감소와 F-score 88% 증가라는 state-of-the-art reconstruction accuracy를 보이며, arbitrary topology를 갖는 고해상도 세부 3D shape 생성도 시연한다.**

By enabling high-resolution, differentiable mesh reconstruction and generation with rendering losses, SparseFlex significantly advances the state-of-the-art in 3D shape representation and modeling.

**SparseFlex는 rendering loss를 사용하는 고해상도 differentiable mesh reconstruction과 generation을 가능하게 함으로써 3D shape representation 및 modeling의 state of the art를 크게 진전시킨다.**

Please see our project page at https://xianglonghe.github.io/TripoSF.

**프로젝트 페이지는 https://xianglonghe.github.io/TripoSF 에서 확인할 수 있다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 재검토했다.

1. Introduction
2. Related Work
   1. 3D Shape Representations for Generation
   2. 3D Generative Models and VAE
3. Method
   1. SparseFlex Representation
   2. SparseFlex VAE for Shape Modeling
   3. Training SparseFlex VAE
   4. Image-to-3D Generation with Rectified Flow
4. Experiments
   1. Implementation Details
   2. Dataset, Baselines, and Metrics
   3. VAE Reconstruction Evaluation
   4. Image to 3D Generation
   5. Ablation Studies
5. Conclusion
6. References

## 요약

### 1. 전체 구조

이 논문은 "고품질 3D asset generation에서 mesh를 직접 다루고 싶지만, watertight conversion과 dense grid memory가 발목을 잡는다"는 문제의식에서 출발한다. 기존 SDF/occupancy 기반 VAE는 대부분 watertight mesh를 전제로 하며, open surface가 많은 실제 asset, 예를 들어 옷, 꽃, 얇은 구조물, 내부 구조가 있는 객체에서는 세부 형상이 사라지거나 표면 추출이 불안정해진다.

SparseFlex의 중심 아이디어는 FlexiCubes 계열의 differentiable isosurface extraction을 dense grid 전체에 적용하지 않고, surface 근처의 sparse voxel set에만 적용하는 것이다. 그 결과 representation은 다음 세 요소로 요약된다.

$$
S = (V, F_c, F_v), \quad F_c = \{s_j, \delta_j\}, \quad F_v = \{\alpha_i, \beta_i\}
$$

여기서 $V$는 sparse voxel center set, $F_c$는 corner grid의 SDF 값과 deformation, $F_v$는 voxel별 interpolation weight를 나타낸다. 추출은 전체 grid가 아니라 $V$에 포함된 sparse voxel에 대해서만 Dual Marching Cubes/FlexiCubes style로 수행된다.

논문은 이 representation을 기반으로 두 가지 시스템을 만든다.

- SparseFlex VAE: point cloud를 sparse voxel feature로 encoding하고, decoder가 SparseFlex parameters를 예측해 rendering loss로 학습한다.
- Image-to-3D generation pipeline: TRELLIS와 유사하게 structure flow model과 structured latent flow model을 사용하되, 최종 geometry decoder를 SparseFlex VAE로 둔다.

### 2. Section 간 연결

Introduction은 implicit field와 rendering-supervised generation의 병목을 분리해서 설명한다. implicit field는 watertight preprocessing과 isosurfacing artifact가 문제이고, rendering supervision은 watertight conversion을 피할 수 있지만 고해상도 dense representation에서는 memory가 터진다. 이 두 문제를 동시에 해결하기 위해 sparse, differentiable, rendering-trainable isosurface representation이 필요하다는 논리로 Method로 넘어간다.

Related Work는 representation 선택지를 세 갈래로 정리한다. Point cloud는 획득과 처리에는 좋지만 surface/solid representation이 약하고, triangle mesh autoregressive 모델은 high face-count mesh에서 어렵고, implicit field는 고품질 mesh를 만들 수 있지만 open surface와 watertight conversion에 약하다. Open surface 쪽에서는 UDF, Surf-D, 3PSDF를 논의하며, 이들이 gradient instability, discontinuity, dense grid limitation을 갖는다고 본다.

Method는 세 단계로 이어진다.

1. Dense FlexiCubes를 sparse voxel 구조로 바꿔 고해상도와 open boundary pruning을 가능하게 한다.
2. SparseFlex를 VAE decoder output으로 삼아 point cloud input에서 mesh를 복원한다.
3. Rendering supervision 학습 시 전체 mesh를 추출하지 않고 view frustum 안의 active voxel만 추출하는 frustum-aware sectional voxel training을 도입한다.

Experiments는 representation 자체의 reconstruction 성능과 generative model의 downstream utility를 모두 본다. 즉 SparseFlex VAE가 reconstruction에서 좋은지, 그리고 이 VAE latent를 기반으로 image-to-3D generation을 했을 때도 경쟁력이 있는지를 분리해 검증한다.

### 3. 핵심 주장과 근거

핵심 주장은 세 가지이다.

첫째, SparseFlex는 open surface와 arbitrary topology를 다루는 differentiable mesh representation이다. dense FlexiCubes처럼 corner SDF, deformation, interpolation weight를 쓰지만, voxel set $V$를 surface-adjacent sparse set으로 제한한다. open boundary 근처의 불필요한 voxel을 pruning할 수 있기 때문에 watertight shape을 강제하지 않는다.

둘째, frustum-aware sectional voxel training은 rendering supervision의 memory 병목을 완화한다. 기존 rendering-supervised mesh learning은 특정 view를 render하기 위해서도 전체 grid에서 mesh를 추출해야 한다. SparseFlex는 sparse voxel 단위로 partial extraction이 가능하므로, camera frustum 안에 들어오는 voxel만 활성화한다.

$$
V_{\mathrm{active}} = \{v_i \mid \mathbb{I}(v_i \in \mathrm{Frustum}(\mathrm{MVP})) = 1,\; v_i \in V\}
$$

셋째, 이 전략은 interior reconstruction까지 가능하게 한다. camera를 object 내부에 배치하거나 near clipping plane을 mesh와 교차시키면, 외부 표면뿐 아니라 내부 구조도 rendering supervision으로 관찰할 수 있다. 이 부분은 일반적인 watertight implicit representation과의 차별점으로 제시된다.

근거는 정량 실험과 ablation이다. Toys4k와 Dora Benchmark에서 Ours256만으로도 주요 baseline보다 좋은 CD/F-score를 보이고, Ours512와 Ours1024로 갈수록 성능이 증가한다. Deepfashion3D open-surface benchmark에서도 self-pruning upsampling을 사용하는 구성의 성능이 더 좋다. Table 3에서는 sparse structure와 frustum-aware sectional voxel training이 없으면 $1024^3$에서 OOM이 발생하는 반면, SparseFlex는 $1024^3$ feed-forward를 수행한다.

### 4. Robotics 관점의 novelty와 relevance

Robotics에서 이 논문의 가치는 "asset generation"보다 "실세계 물체 geometry를 robot이 쓰기 좋은 mesh로 만들 가능성"에 있다.

- Open surface: 의류, 가방, 케이블, 얇은 플라스틱, 식물, sheet metal 같은 객체는 watertight solid로 닫기 어렵다. SparseFlex의 open boundary pruning은 이런 객체군에 직접적 관련이 있다.
- Interior structure: grasp planning, insertion, inspection, simulation에서 내부 홈, 구멍, cavity, layered structure가 중요할 수 있다. 논문은 rendering supervision만으로 interior를 다룰 수 있다고 주장한다.
- Differentiable mesh: rendering loss 기반이므로 RGB-D, normal, mask supervision과 결합하기 쉽고, robot perception pipeline에서 differentiable reconstruction module로 확장할 수 있다.
- Simulation-ready geometry 가능성: mesh output은 point cloud나 Gaussian보다 collision, FEM, contact simulation으로 넘기기 쉽다. 다만 논문 자체가 physical validity, manifoldness, self-intersection, collision stability를 직접 검증하지는 않는다.

현실 배치 관점에서 가장 큰 제약은 compute와 data이다. 논문은 SparseFlex VAE를 64 A100에서 학습했고, training data도 약 400K high-quality mesh를 사용한다. 따라서 robot lab에서 직접 end-to-end 재학습하기보다는 pre-trained geometry prior로 사용하거나, 제한된 category에 fine-tuning하는 방식이 더 현실적이다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | 본 논문 | 의미 |
|---|---|---|---|
| Watertight SDF/occupancy | SDF/occupancy 학습 전 watertight conversion이 필요하고 fine detail이 손상될 수 있음 | rendering loss로 직접 SparseFlex mesh를 학습 | raw/open mesh detail 보존 가능성이 큼 |
| UDF/open-surface methods | open surface를 표현할 수 있지만 gradient estimation과 surface extraction이 불안정할 수 있음 | sparse FlexiCubes-style isosurface로 open surface를 표현 | explicit mesh extraction 안정성과 open topology를 함께 노림 |
| Dense FlexiCubes | differentiable하고 sharp feature에 강하지만 dense grid memory가 큼 | surface-adjacent sparse voxel에 FlexiCubes parameter를 둠 | $1024^3$급 고해상도 학습을 주장 |
| TRELLIS류 structured latent | scalable 3D latent generation에 강하지만 geometry fidelity와 open surface 처리에 한계 | point cloud 기반 SparseFlex VAE와 self-pruning upsampling 사용 | generation prior의 decoder fidelity를 개선 |
| 3PSDF | open surface에 특화되지만 binary occupancy extraction 때문에 discontinuity/artifact가 생길 수 있음 | SDF, deformation, interpolation weights를 sparse voxel에서 예측 | open boundary와 세부 구조 복원 품질을 개선 |

정량 결과의 핵심 수치는 다음과 같다.

| 평가 | 주요 비교 | 결과 요약 |
|---|---|---|
| Toys4k VAE reconstruction | Craftsman, Dora, TRELLIS, XCube, 3PSDF | Ours1024가 CD 1.33/0.60, F1(0.001) 25.95/35.69, F1(0.01) 92.30/96.22로 최고권 성능 |
| Dora Benchmark VAE reconstruction | 같은 baseline | Ours1024가 CD 0.86/0.12, F1(0.001) 25.71/39.50, F1(0.01) 94.71/99.14 |
| Deepfashion3D open surface | Surf-D, 3PSDF | self-pruning upsampling을 둔 Ours1024가 CD 0.04, F1(0.001) 37.22, F1(0.01) 100.00 |
| Generation on Toys4k | InstantMesh, Direct3D, TRELLIS | Ours가 FID 44.95, KID $1.05 \times 10^{-3}$로 가장 낮음 |
| Memory/runtime ablation | w/o FSV, w/o FSV & sparse | $1024^3$에서 baseline ablation은 OOM, Ours는 visibility ratio $0.1$에서 1151 ms, 55441 MB |

Table 1의 `/` 표기는 전체 dataset 결과와 watertight subset 결과를 나눈 것이다. Dora와 Craftsman처럼 watertight data 중심으로 학습된 방법은 전체 non-watertight object가 포함될 때 성능 저하가 크며, 논문은 이를 open surface 대응력의 근거로 사용한다.

### 6. Implementation idea

SparseFlex VAE의 구현 흐름은 다음과 같이 읽을 수 있다.

1. Mesh surface에서 point cloud $P = \{p_i \in \mathbb{R}^3\}_{i=1}^{N_p}$와 normal $N = \{n_i \in \mathbb{R}^3\}_{i=1}^{N_p}$를 sampling한다.
2. Point cloud를 voxelize하여 sparse voxel structure $V$를 만든다.
3. 각 voxel 내부 point에 shallow PointNet과 local max-pooling을 적용해 voxel feature $f_i$를 만든다.
4. Sparse transformer encoder가 feature set $F=\{f_i\}$와 structure $V$를 받아 latent code $z \in \mathbb{R}^{d_z}$를 만든다.
5. Decoder가 transformer layer와 linear head를 통해 corner SDF $s_j$, deformation $\delta_j$, voxel interpolation weights $\alpha_i, \beta_i$를 예측한다.
6. 두 개의 convolutional self-pruning upsampling module이 voxel resolution을 단계적으로 올리고, predicted occupancy를 기준으로 redundant voxel을 제거한다.
7. Rendering loss 계산 시 camera frustum 안의 $V_{\mathrm{active}}$만 사용해 isosurface extraction과 rendering을 수행한다.
8. Depth, normal, mask, SSIM, LPIPS 기반 rendering loss와 structure pruning loss, KL regularization, FlexiCubes regularization을 함께 최적화한다.

Image-to-3D generation은 두 flow model을 연결한다. 먼저 structure flow model이 DINOv2 image feature를 cross-attention으로 받아 low-resolution sparse structure를 생성한다. 다음 structured latent flow model이 image condition과 sparse structure를 함께 사용해 SparseFlex VAE latent를 생성하고, VAE decoder가 최종 mesh를 만든다.

### 7. Mathematical background

SparseFlex representation은 dense grid 전체가 아니라 $N_v$개의 active/sparse voxel과 그 주변 corner grid만을 대상으로 한다. Dense FlexiCubes가 resolution $N_r^3$ voxel과 $N_g^3$ corner grid를 갖는다면, SparseFlex에서는 보통 $N_v \ll N_r^3$이고 $N_c \ll N_g^3$이므로 memory가 줄어든다.

논문이 제시하는 representation은 다음과 같다.

$$
S = (V, F_c, F_v), \quad F_c = \{s_j, \delta_j\}, \quad F_v = \{\alpha_i, \beta_i\}
$$

학습 objective는 네 항으로 구성된다.

$$
L = \lambda_1 L_{\mathrm{render}} + \lambda_2 L_{\mathrm{prune}} + \lambda_3 L_{\mathrm{KL}} + \lambda_4 L_{\mathrm{flex}}
$$

Rendering loss는 differentiable rendering에서 쓰는 depth, normal, mask, SSIM, LPIPS 항의 weighted sum이다.

$$
L_{\mathrm{render}} =
\lambda_d L_d +
\lambda_n L_n +
\lambda_m L_m +
\lambda_{ss} L_{ss} +
\lambda_{lp} L_{lp}
$$

$L_d$, $L_n$, $L_m$은 각각 depth map, normal map, mask map의 $L_1$ loss이고, $L_{ss}$와 $L_{lp}$는 normal map에 적용되는 SSIM loss와 LPIPS loss이다.

Pruning loss는 sparse voxel structure를 supervision하기 위한 BCE loss이다.

$$
L_{\mathrm{prune}} = \mathrm{BCE}(V, \hat{V})
$$

여기서 $V$는 input point cloud에서 얻은 ground-truth voxel occupancy이고, $\hat{V}$는 upsampling module이 예측한 occupancy이다. $L_{\mathrm{KL}}$은 VAE latent distribution을 standard normal prior에 맞추는 KL divergence이며, $L_{\mathrm{flex}}$는 FlexiCubes에서 온 regularization으로 smooth SDF 값을 유도한다.

Frustum-aware training의 active voxel set은 다음처럼 정의된다.

$$
V_{\mathrm{active}} =
\{v_i \mid \mathbb{I}(v_i \in \mathrm{Frustum}(\mathrm{MVP})) = 1,\; v_i \in V\}
$$

Adaptive frustum은 visibility ratio $\gamma$, $0 < \gamma \leq 1$로 active voxel 비율을 제어한다. near/far clipping plane을 반복적으로 조정해 목표 active voxel 수에 맞추고, 이로써 memory와 reconstruction detail 사이의 trade-off를 조절한다.

### 8. Experiments

**Implementation details.** 저자들은 FlexiCubes official code를 기반으로 SparseFlex를 구현했다. 학습 데이터는 Objaverse와 Objaverse-XL에서 필터링한 약 400K high-quality 3D mesh이다. raw data의 flipped normal이 VAE reconstruction과 generation 모두를 악화시킬 수 있어서, outward normal이 일관되도록 mesh preprocessing을 수행한다.

SparseFlex VAE는 progressive training으로 최종 resolution을 256, 512, 1024 순서로 높인다. Structure VAE와 structure flow model은 TRELLIS model을 채택하고 pre-trained weights를 fine-tuning한다. SparseFlex VAE 학습은 64 A100, batch size 64이고, structured latent flow model은 batch size 256이다. Optimizer는 AdamW, initial learning rate는 $1 \times 10^{-4}$, weight decay는 0.01이다. Inference에서는 CFG 3.5와 50 sampling steps를 사용한다.

**Datasets.** VAE reconstruction은 ABO, GSO, Meta, Objaverse, Toys4k, Deepfashion3D에서 평가한다. ABO, GSO, Meta, Objaverse test list는 Dora benchmark에서 가져오되 training data 약 2.7K assets를 제외한다. Toys4k는 TRELLIS 설정을 따른다. Image-to-3D generation은 Toys4k의 random 200 assets와 in-the-wild image로 평가한다.

**Baselines.** VAE reconstruction baseline은 Craftsman, TRELLIS, Dora, XCube, Surf-D, 3PSDF이다. Surf-D와 3PSDF는 open surface에 특화된 방법이다. Generation baseline은 InstantMesh, Direct3D, TRELLIS이다.

**Metrics.** Reconstruction은 Chamfer Distance와 F-score threshold 0.01/0.001을 사용한다. 논문에서는 CD와 F-score를 각각 $10^4$, $10^2$ scale로 보고한다. Generation은 normal map의 네 orthogonal view를 render한 뒤 FID와 KID를 계산한다.

**VAE reconstruction.** Table 1에서 Ours256, Ours512, Ours1024가 resolution 증가에 따라 꾸준히 좋아진다. 특히 Ours1024는 Toys4k와 Dora Benchmark 모두에서 가장 낮은 CD와 높은 F-score를 보인다. 저자들은 이전 방법 대비 CD 82% 감소, F-score 88% 증가를 강조한다. Qualitative comparison에서도 complex shape, open surface, interior structure에서 surface error가 줄어드는 모습을 보인다.

**Open-surface reconstruction.** Deepfashion3D에서는 3PSDF와 Surf-D를 포함해 비교한다. Self-pruning upsampling이 있는 Ours1024가 CD 0.04, F1(0.001) 37.22, F1(0.01) 100.00으로 가장 좋다. 논문은 self-pruning upsampling이 open boundary 근처 voxel을 잘 제거해 input boundary와 reconstruction boundary를 맞추는 데 중요하다고 해석한다.

**Image-to-3D generation.** Toys4k generation에서는 Ours가 FID 44.95, KID $1.05 \times 10^{-3}$으로 InstantMesh, Direct3D, TRELLIS보다 낮다. 논문은 SparseFlex VAE의 geometry fidelity가 downstream generation 품질로 이어진다고 주장한다.

**Ablation.** Table 3은 SparseFlex와 frustum-aware sectional voxel training의 memory/runtime 효과를 보여준다. Visibility ratio $\gamma=0.1$에서 Ours는 256, 512, 1024 resolution에 대해 feed-forward time 333 ms, 620 ms, 1151 ms와 GPU memory 35515 MB, 40183 MB, 55441 MB를 기록한다. $\gamma=0.3$이면 memory와 time이 증가한다. Frustum-aware sectional voxel training이 없으면 $1024^3$에서 OOM이고, sparse structure까지 없으면 $512^3$부터 OOM이다.

### 9. Limitations and future work

논문이 직접 밝히는 한계는 세 가지이다.

- Open surface boundary는 voxel pruning으로 처리되지만 낮은 resolution에서는 minor artifact가 남을 수 있다.
- High-resolution generation은 여전히 computationally demanding하다.
- Interior structure generation에 대한 더 정밀한 control은 future work이다.

추가로 연구자가 주의해서 볼 지점은 다음과 같다.

- Reconstruction metric은 geometry fidelity 중심이고, downstream robotics simulation에서 중요한 manifoldness, self-intersection, collision stability, physical material consistency는 검증하지 않는다.
- Rendering supervision으로 interior를 볼 수 있다는 주장은 camera placement나 clipping plane 설계에 의존한다. 실제 robot perception에서는 내부를 관찰할 수 있는 sensor path나 data acquisition protocol이 별도로 필요하다.
- 64 A100 학습과 400K mesh data는 상당한 compute/data regime이다. 산업/연구실 적용에서는 pretrained prior를 활용하는 방향이 현실적이다.
- Image-to-3D generation 평가는 FID/KID와 qualitative result 중심이다. 생성된 mesh가 CAD/robotics toolchain에 바로 들어갈 정도로 clean한지에 대한 별도 검증은 부족하다.

### 10. 결론

SparseFlex는 FlexiCubes의 differentiable isosurface extraction을 sparse voxel 구조와 결합해, open surface와 arbitrary topology를 갖는 고해상도 mesh reconstruction/generation을 노리는 논문이다. 기술적 핵심은 sparse representation 자체와 frustum-aware sectional voxel training의 결합이며, 이 조합이 rendering-supervised 학습의 memory 병목을 줄이고 $1024^3$ resolution 및 interior reconstruction을 가능하게 한다는 점이다.

AI/robotics 연구 관점에서는 "watertight conversion 없이 open-surface mesh를 고해상도로 복원하는 differentiable geometry prior"로 읽는 것이 가장 유용하다. 다만 실제 robot deployment를 위해서는 reconstruction 품질뿐 아니라 mesh validity, contact/simulation 안정성, sensor visibility, compute budget에 대한 추가 검증이 필요하다.

## 추가 질문과 답변
