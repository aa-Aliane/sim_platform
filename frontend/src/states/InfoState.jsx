import create from "zustand";

export const infoStore = create((set) => ({
  infos: [],
  initInfo: (infos) =>
    set((state) => ({
      infos: infos,
    })),
  switchVal: (index) =>
    set((state) => ({
      infos: state.infos.map((info, i) => {
        if (i === index) return "true";
        return "false";
      }),
    })),
}));
