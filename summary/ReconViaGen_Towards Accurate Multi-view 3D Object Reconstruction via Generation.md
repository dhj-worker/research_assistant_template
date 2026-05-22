# ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation

## 메타데이터

- PDF 파일: `ReconViaGen_Towards Accurate Multi-view 3D Object Reconstruction via Generation.pdf`
- 논문 제목: ReconViaGen: Towards Accurate Multi-view 3D Object Reconstruction via Generation
- 저자: Jiahao Chang, Chongjie Ye, Yushuang Wu, Yuantao Chen, Yidan Zhang, Zhongjin Luo, Chenghong Li, Yihao Zhi, Xiaoguang Han
- 소속: The Chinese University of Hong Kong, Shenzhen; The Future Network of Intelligence Institute, CUHK-Shenzhen
- venue/arXiv: arXiv:2510.23306v1 [cs.CV]
- 연도: 2025
- DOI/URL: DOI 확인 필요; Project page `https://jiahao620.github.io/reconviagen`
- 작업 일시: 2026-05-22 14:15

## Abstract

Existing multi-view 3D object reconstruction depends strongly on sufficient view overlap, so sparse or occluded captures often produce incomplete shapes.

**기존 multi-view 3D object reconstruction은 입력 view 사이의 충분한 overlap에 크게 의존하므로, 실제 환경의 occlusion이나 sparse coverage에서는 심각하게 불완전한 3D 결과가 자주 발생한다.**

Recent diffusion-based 3D generation can use learned priors to infer invisible object parts and produce plausible full structures.

**최근 diffusion 기반 3D generative technique은 학습된 generative prior로 보이지 않는 물체 부분을 추론하여 그럴듯한 완전 구조를 생성할 수 있다.**

However, stochastic diffusion inference reduces accuracy and reliability, making such priors hard to plug into reconstruction systems.

**하지만 diffusion inference의 stochastic nature는 결과의 정확도와 신뢰성을 떨어뜨리며, 이 때문에 기존 reconstruction framework가 3D generative prior를 안정적으로 통합하기 어렵다.**

The paper analyzes two causes of poor consistency: weak cross-view conditioning and limited controllability of iterative denoising for local details.

**논문은 diffusion 기반 3D generation이 input consistency를 잘 맞추지 못하는 원인을 두 가지로 분석한다: multi-view image feature를 condition으로 만들 때 cross-view connection을 충분히 구성·활용하지 못하는 점, 그리고 local detail generation에서 iterative denoising의 controllability가 낮아 fine geometry와 texture가 입력과 어긋나는 점이다.**

ReconViaGen integrates reconstruction priors into a generative framework and introduces strategies to address these issues.

**ReconViaGen은 reconstruction prior를 generative framework 안으로 통합하고, 위 문제들을 완화하기 위한 여러 설계를 제안한다.**

Experiments show that ReconViaGen reconstructs complete and accurate 3D models aligned with input views in both global structure and local detail.

**실험 결과 ReconViaGen은 global structure와 local detail 양쪽에서 입력 view와 일관적인 완전하고 정확한 3D model을 재구성한다.**

The project page is provided by the authors.

**저자들은 project page를 함께 제공한다.**

## 목차

> 본문 heading 기반으로 재구성했으며, section/subsection 누락 여부를 `full.txt`에서 다시 확인했다.

1. Introduction
2. Related Work
   1. Single-view 3D Generation
   2. Multi-view 3D Reconstruction
   3. Combination of Generation and Reconstruction
3. Methodology
   1. Preliminary
   2. Reconstruction-based Conditioning
   3. Coarse-to-fine Generation
4. Experiments
   1. Experiment Setup
   2. Experiment Results
   3. Ablation Study
5. References
6. Appendix
   1. Details on Camera Pose Estimation
   2. Evaluation with More Input Images
   3. Evaluation of Camera Pose Estimation
   4. Ablation Study on the Number of Input Images
   5. Ablation Study on the Form of Condition
   6. Reconstruction on Generated Multi-view Images or Videos
   7. More Reconstruction Results
   8. The Use of Large Language Models

## 요약

### 1. 전체 구조

이 논문은 pose-free multi-view object reconstruction을 “순수 reconstruction의 불완전성”과 “diffusion generation의 입력 불일치” 사이의 간극으로 정의한다. 기존 MVS, NeRF, DUSt3R/VGGT 계열은 관측된 영역의 geometry cue에는 강하지만 occlusion, support surface, weak texture, sparse capture 상황에서 hole과 누락이 생긴다. 반대로 TRELLIS, Hunyuan3D 같은 diffusion 기반 3D generator는 보이지 않는 부분을 그럴듯하게 hallucinate할 수 있지만, stochastic denoising 때문에 pixel-level input alignment가 약하다.

ReconViaGen의 핵심 구조는 VGGT의 reconstruction prior와 TRELLIS의 generation prior를 한 pipeline 안에서 결합하는 것이다. VGGT는 입력 multi-view image에서 pose, depth, point map, tracking feature를 암묵적으로 담은 3D-aware feature를 제공하고, TRELLIS는 sparse structure flow와 SLAT flow를 통해 complete 3D asset을 생성한다. 논문은 이 둘을 단순 cascade로 연결하지 않고, VGGT feature를 diffusion condition으로 가공해 coarse-to-fine generation 전체에 주입한다.

전체 pipeline은 세 단계다.

1. VGGT feature에서 global geometry condition과 local per-view condition을 만든다.
2. Global geometry condition은 TRELLIS의 SS Flow에 넣어 coarse sparse structure를 만들고, local per-view condition은 SLAT Flow에 넣어 fine geometry와 texture를 만든다.
3. Inference에서 생성 결과와 입력 view를 rendering으로 비교하고, Rendering-aware Velocity Compensation으로 SLAT denoising trajectory를 보정한다.

### 2. Section 간 연결

Introduction은 왜 기존 reconstruction과 generation이 각각 실패하는지 문제를 나눈다. Related Work는 single-view 3D generation, multi-view reconstruction, generation-reconstruction 결합 연구를 훑은 뒤, diffusion prior의 detail quality와 reconstruction prior의 input consistency가 아직 제대로 결합되지 않았다는 빈틈을 만든다.

Methodology는 먼저 두 prior를 정리한다. VGGT는 pose-free reconstruction prior이고, TRELLIS는 SLAT 기반 3D native generative prior다. 그다음 VGGT feature를 diffusion condition으로 바꾸는 두 condition을 제안한다. 마지막으로 SS Flow, SLAT Flow, RVC가 각각 global shape, local detail, pixel-level alignment를 맡도록 연결한다.

Experiments는 이 설계가 실제로 generation baseline과 reconstruction baseline을 모두 넘는지 검증한다. Table 1은 Dora-Bench와 OmniObject3D에서의 정량 비교를 제공하고, Table 2와 appendix ablation은 GGC, PVC, RVC 각각의 역할을 분리해 보여준다.

### 3. 핵심 주장과 근거

**주장 1: Multi-view reconstruction에는 generative prior가 필요하다.** VGGT 같은 feed-forward reconstruction은 pose-free setting에서 강하지만 point cloud 기반 결과의 incompleteness가 남는다. 논문은 Dora-Bench와 OmniObject3D에서 VGGT가 geometry metric은 강하지만 rendering consistency metric을 직접 제공하지 못하고, unseen part completion에는 한계가 있다고 본다.

**주장 2: Diffusion prior는 그대로 쓰면 reconstruction에 충분히 정확하지 않다.** TRELLIS-S는 각 denoising step에서 임의 view를 condition으로 쓰고, TRELLIS-M은 multi-diffusion 방식으로 평균 denoised result를 쓰지만, 두 방식 모두 global structure와 local detail의 input consistency가 부족하다. 논문은 원인을 cross-view correlation 부족과 denoising controllability 부족으로 설명한다.

**주장 3: VGGT feature를 condition으로 직접 쓰되, coarse와 fine 단계에 서로 다른 형태로 넣어야 한다.** Global Geometry Condition은 all-view VGGT feature를 고정 길이 token list로 aggregate해 SS Flow의 coarse geometry를 안정화한다. Local Per-View Condition은 view별 token list를 만들어 SLAT Flow에서 texture와 fine geometry alignment를 살린다.

**주장 4: Inference-time rendering constraint가 local alignment를 더 끌어올린다.** RVC는 생성 중간 결과를 rendering하고 input image와의 SSIM, LPIPS, DreamSim loss를 사용해 SLAT velocity를 보정한다. Table 2에서 RVC를 추가하면 PSNR, SSIM, LPIPS, CD, F-score가 모두 full model 성능으로 개선된다.

### 4. Robotics 관점의 novelty와 relevance

로봇 관점에서 중요한 지점은 이 논문이 “정확한 관측 영역”과 “완전한 비관측 영역”을 동시에 노린다는 점이다. Manipulation, grasp planning, object rearrangement, scene editing에서는 보이는 표면만 맞는 point cloud보다 occluded backside와 support-contact 주변 geometry가 그럴듯하게 완성된 mesh가 더 유용할 수 있다. ReconViaGen은 diffusion prior로 completeness를 확보하되, VGGT와 RVC로 input-view consistency를 회복하려 한다.

Pose-free multi-view 입력을 받는 것도 실사용 relevance가 있다. 로봇 wrist camera나 handheld scanner에서는 calibration이 완벽하지 않고, 물체 주변의 view coverage도 균일하지 않다. 이 논문은 VGGT 기반 pose estimation과 refinement를 사용해 camera pose 없이 들어온 multi-view를 TRELLIS generation space에 등록한다.

다만 robotics deployment에는 남는 리스크가 있다. Diffusion prior가 invisible part를 hallucinate하므로, 실제 물체의 functional geometry나 contact-critical geometry를 보장하지 않는다. 실험은 object benchmark 중심이며, 물리적 안정성, collision, grasp success, metric-scale accuracy, sensor noise, reflective/transparent objects에 대한 검증은 확인 필요다. 따라서 로봇 파이프라인에서는 final geometry를 planning ground truth로 바로 쓰기보다, uncertainty-aware completion 또는 perception proposal로 쓰는 편이 안전하다.

### 5. 기존 방법과 비교

| 구분 | 기존 방법 | 본 논문 | 의미 |
|---|---|---|---|
| Pure reconstruction | VGGT, DUSt3R 계열은 pose-free geometry cue와 camera estimation에 강하지만 incomplete point cloud/blurred detail 문제가 남음 | VGGT feature를 condition으로 쓰고 TRELLIS prior로 invisible region을 completion | Reconstruction의 관측 정합성과 generation의 완전성을 결합 |
| Diffusion generation | TRELLIS-S/M은 plausible 3D를 만들지만 multi-view input consistency가 약함 | GGC/PVC/RVC로 cross-view-aware diffusion condition과 rendering-aware denoising 보정 | Stochastic generation을 reconstruction-friendly하게 제어 |
| Fixed-view large reconstruction | InstantMesh, LGM은 fixed viewpoint assumption이 강함 | Arbitrary input views와 pose-free setting을 지원 | 로봇/실세계 capture처럼 viewpoint가 통제되지 않는 상황에 더 적합 |
| Commercial generator | Hunyuan3D-2.5, Meshy-5는 qualitative 비교에서 orthogonal viewpoint 요구가 있음 | In-the-wild multi-view에서도 arbitrary camera pose를 받을 수 있다고 주장 | controlled capture가 어려운 workflow에서 장점 |

주요 Table 1 결과는 다음과 같다.

| Method | Dora PSNR | Dora LPIPS | Dora CD | Dora F-score | Omni PSNR | Omni LPIPS | Omni CD | Omni F-score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| TRELLIS-S | 16.562 | 0.103 | 0.176 | 0.807 | 16.021 | 0.264 | 0.102 | 0.906 |
| TRELLIS-M | 16.706 | 0.111 | 0.144 | 0.843 | 16.861 | 0.242 | 0.072 | 0.932 |
| Hunyuan3D-2.0-mv | 20.221 | 0.093 | 0.094 | 0.937 | 16.665 | 0.165 | 0.124 | 0.871 |
| InstantMesh | 18.922 | 0.120 | 0.110 | 0.865 | 17.499 | 0.145 | 0.094 | 0.907 |
| LucidFusion | 16.509 | 0.144 | 0.131 | 0.831 | 16.254 | 0.144 | 0.114 | 0.868 |
| ReconViaGen | 22.632 | 0.090 | 0.0895 | 0.953 | 19.767 | 0.141 | 0.059 | 0.959 |

해석하면 ReconViaGen은 Dora-Bench에서 Hunyuan3D-2.0-mv 대비 PSNR을 크게 올리고 CD를 낮춘다. OmniObject3D에서는 LPIPS가 LucidFusion보다 약간 높지만, PSNR, CD, F-score에서 가장 강한 결과를 보인다. 즉 perceptual texture metric 한 항목에서는 압도적이지 않지만, geometry accuracy와 completeness에는 강한 증거가 있다.

### 6. Implementation idea

구현 흐름은 다음처럼 볼 수 있다.

1. 입력: calibration 없는 $N$개의 object multi-view image.
2. Object dataset으로 VGGT aggregator를 LoRA fine-tuning한다. Loss는 camera, depth, point map loss를 합친 multi-task objective다.
3. Fine-tuned VGGT에서 여러 layer의 3D-aware feature를 추출한다.
4. Condition Net으로 all-view feature를 aggregate해 Global Geometry Condition $T_g$를 만든다.
5. View별 Condition Net으로 Local Per-View Condition $\{T_k\}$를 만든다.
6. TRELLIS SS Flow는 $T_g$를 cross-attention condition으로 받아 sparse voxel structure를 생성한다.
7. TRELLIS SLAT Flow는 $\{T_k\}$를 view-wise cross-attention condition으로 받아 active voxel의 latent와 texture/detail을 생성한다.
8. SLAT를 intermediate 3D output으로 decode하고, VGGT/TRELLIS space에 camera pose를 refine한다.
9. Rendering-aware Velocity Compensation으로 input render loss를 velocity update에 반영한다.
10. 최종 SLAT를 mesh, 3DGS, radiance field 등으로 decode한다. 논문 실험에서는 textured mesh 중심으로 서술된다.

학습 세부사항도 꽤 무겁다. Objaverse 390k 3D data를 사용하고, object mesh당 150개 view를 $512 \times 512$로 render한다. VGGT와 TRELLIS transformer에는 LoRA rank $64$, alpha $128$, dropout $0$을 적용하며, qkv mapping layer와 attention projector에 adapter를 붙인다. SS Flow fine-tuning은 TRELLIS 기반, classifier-free guidance drop rate $0.3$, AdamW learning rate $10^{-4}$, 8개 NVIDIA A800 80GB, batch size $192$, 40k steps다. Inference에서는 SS generation CFG $7.5$, SLAT generation CFG $3.0$, sampling step $30/12$, RVC coefficient $\lambda=0.1$을 사용한다.

### 7. Mathematical background

VGGT LoRA fine-tuning objective는 camera pose, depth, point map loss를 함께 최적화한다.

$$
L_{\mathrm{VGGT}}(\theta)
= L_{\mathrm{camera}} + L_{\mathrm{depth}} + L_{\mathrm{pmap}}
$$

TRELLIS의 conditional flow matching은 noisy state $x_t$와 target $x_0$ 사이의 velocity field를 학습한다. PDF extraction에서 일부 기호가 깨졌지만, 논문 의도는 rectified flow의 predicted velocity가 target direction을 맞추도록 하는 objective다.

$$
L_{\mathrm{CFM}}(\theta)
= \mathbb{E}_{t, x_0}
\left[
\left\| v_{\theta}(x_t, t) - (\epsilon - x_0) \right\|_2^2
\right]
$$

Global Geometry Condition은 learnable token list가 VGGT feature에 cross-attention하면서 만들어진다.

$$
\begin{aligned}
T^{i+1}
&= \mathrm{CrossAttn}
\left(
Q(T^i), K(\phi_{\mathrm{VGGT}}), V(\phi_{\mathrm{VGGT}})
\right), \\
i &\in \{0, 1, 2, 3\}.
\end{aligned}
$$

Local Per-View Condition은 같은 구조를 view별 VGGT feature에 적용한다.

$$
\begin{aligned}
T_k^{i+1}
&= \mathrm{CrossAttn}
\left(
Q(T_k^i), K(\phi_{\mathrm{VGGT}}^k), V(\phi_{\mathrm{VGGT}}^k)
\right), \\
k &\in \{1, \dots, N\}.
\end{aligned}
$$

SLAT Flow에서는 각 view condition과의 cross-attention 결과를 MLP weight로 fuse한다.

$$
\begin{aligned}
y_{j+1}
&=
\sum_{k=1}^{N}
\mathrm{CrossAttn}
\left(
Q(y_j), K(T_k), V(T_k)
\right)
\cdot w_k .
\end{aligned}
$$

RVC loss는 rendered image와 input image 사이의 structural, perceptual, semantic discrepancy를 합친다.

$$
\begin{aligned}
L_{\mathrm{RVC}}
&= L_{\mathrm{SSIM}} + L_{\mathrm{LPIPS}} + L_{\mathrm{DreamSim}} .
\end{aligned}
$$

현재 timestep에서 predicted target SLAT는 다음처럼 표현된다.

$$
\begin{aligned}
\hat{x}_0
&= x_t - t \cdot v_t .
\end{aligned}
$$

RVC는 이 loss의 gradient로 velocity compensation term을 만들고, 다음 step update에 더한다.

$$
\begin{aligned}
\Delta v_t
&= -\frac{1}{t}
\frac{\partial L_{\mathrm{RVC}}}{\partial \hat{x}_0}, \\
x_{t_{\mathrm{prev}}}
&= x_t - (t - t_{\mathrm{prev}})
\left(
v_t + \lambda \Delta v_t
\right).
\end{aligned}
$$

논문은 pose estimation 오류 영향을 줄이기 위해 per-image loss가 $0.8$보다 큰 경우 해당 image loss를 버린다고 설명한다.

### 8. Experiments

**Datasets.** Training에는 Objaverse 390k 3D data를 사용한다. Evaluation은 Dora-Bench 300 objects와 OmniObject3D 200 objects, 20 categories를 사용한다. OmniObject3D는 24 views 중 무작위 4 views를 input으로 쓰고, Dora-Bench는 TRELLIS trajectory에서 40 views를 render한 뒤 No.0, 9, 19, 29의 4 views를 사용한다.

**Metrics.** Novel view rendering accuracy는 PSNR, SSIM, LPIPS로 평가한다. Geometry accuracy와 completeness는 Chamfer Distance와 F-score로 평가한다. CD/F-score는 100k points sampling, object points를 $[-1, 1]^3$ 범위로 normalize, F-score radius $r=0.1$ 설정을 사용한다.

**Baselines.** TRELLIS-S, TRELLIS-M, Hunyuan3D-2.0-mv, InstantMesh, LGM, LucidFusion, VGGT와 비교한다. 또한 in-the-wild qualitative comparison에서는 closed-source Hunyuan3D-2.5와 Meshy-5도 비교한다.

**Main result.** ReconViaGen은 Dora-Bench에서 PSNR 22.632, SSIM 0.911, LPIPS 0.090, CD 0.0895, F-score 0.953을 기록한다. OmniObject3D에서는 PSNR 19.767, SSIM 0.847, LPIPS 0.141, CD 0.059, F-score 0.959다. 논문은 이 결과가 generation prior와 reconstruction prior의 결합이 두 단독 계열보다 낫다는 증거라고 주장한다.

**Ablation.**

| Variant | GGC | PVC | RVC | PSNR | SSIM | LPIPS | CD | F-score |
|---|---|---|---|---:|---:|---:|---:|---:|
| TRELLIS-M style baseline | no | no | no | 16.706 | 0.882 | 0.111 | 0.144 | 0.843 |
| + GGC | yes | no | no | 20.462 | 0.894 | 0.102 | 0.093 | 0.941 |
| + PVC | yes | yes | no | 21.045 | 0.905 | 0.093 | 0.093 | 0.937 |
| + RVC | yes | yes | yes | 22.632 | 0.911 | 0.090 | 0.089 | 0.953 |

이 ablation은 GGC가 coarse shape accuracy를 크게 끌어올리고, PVC가 local per-view alignment와 PSNR을 추가 개선하며, RVC가 inference-only refinement인데도 shape completeness와 fine-grained appearance를 더 개선함을 보여준다.

**More input views.** Appendix에서 Object VGGT + 3DGS와 비교했을 때 ReconViaGen은 uniform 6/8/10 views에서 PSNR/LPIPS 22.823/0.089, 23.067/0.090, 23.193/0.087을 보인다. Limited-view setting에서도 21.427/0.098, 21.782/0.099, 21.866/0.103으로 Object VGGT + 3DGS보다 높다. 입력 수 ablation에서는 2 views에서 PSNR 19.568, 4 views에서 22.632, 6 views에서 22.823, 8 views에서 23.067로 증가하되 marginal gain은 줄어든다.

**Pose estimation.** Appendix Table 4는 pose refinement가 translation error를 낮추는 데 도움을 준다고 보고한다. VGGT 대비 object VGGT와 Ours가 TE를 개선하며, 다만 Ours의 RRE는 object VGGT보다 약간 높다고 설명한다. 저자들은 generated 3D model과 ground-truth geometry 사이의 작은 mismatch 때문일 수 있다고 해석한다.

### 9. Limitations and future work

논문이 명시적으로 limitation section을 두지는 않지만, 본문과 appendix에서 다음 한계가 드러난다.

- RVC는 pose refinement 품질에 의존한다. 저자들도 inaccurate pose estimation의 영향을 줄이기 위해 loss thresholding을 사용한다.
- Diffusion prior는 invisible region을 plausible하게 완성하지만, 실제 보이지 않은 geometry의 정답성을 보장하지 않는다.
- 실험은 object-centric benchmark와 qualitative in-the-wild 중심이다. 로봇 manipulation 성공률, contact-rich task, physical simulation consistency, metric scale 검증은 확인 필요다.
- Training과 fine-tuning 비용이 크다. 390k 3D data, 8 x A800 80GB, 40k steps는 일반 연구실/로봇 시스템에서 재현 부담이 있다.
- Reflective, transparent, articulated, deformable, heavily occluded object에 대한 robustness는 본문에서 충분히 분리 검증되지 않았다.
- Commercial generator와의 비교는 qualitative 위주이며, closed-source 모델의 exact setting과 reproducibility는 제한적이다.

Future work로는 uncertainty-aware completion, physical plausibility constraint, task-driven reconstruction metric, robot sensor noise augmentation, online/incremental multi-view capture와의 결합이 자연스럽다.

### 10. 결론

ReconViaGen은 “multi-view reconstruction의 정확한 관측 정합성”과 “diffusion 3D generation의 완전한 shape prior”를 결합하려는 논문이다. 방법적으로는 VGGT feature를 global/local condition으로 분해해 TRELLIS의 SS Flow와 SLAT Flow에 주입하고, inference 단계에서 rendering-aware velocity compensation으로 denoising trajectory를 input view 쪽으로 끌어당기는 것이 핵심이다.

정량 결과는 꽤 설득력 있다. Dora-Bench와 OmniObject3D에서 geometry accuracy와 completeness가 강하고, ablation도 GGC/PVC/RVC의 역할을 단계적으로 뒷받침한다. Robotics 관점에서는 pose-free arbitrary-view object reconstruction과 occluded part completion에 매력이 있지만, diffusion hallucination이 실제 물리 geometry를 보장하지 않는다는 점 때문에 downstream planning에는 uncertainty와 validation을 함께 붙여야 한다.

## 추가 질문과 답변
