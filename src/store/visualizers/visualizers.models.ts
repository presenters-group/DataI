export interface IVisualizer {
  data: number;
  usedColumns: number[];
  usedRow: number;
  chart: string;
  name: string;
  filters: any[];
  isDeleted: boolean;
}
